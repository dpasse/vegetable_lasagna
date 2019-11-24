import luigi
import json
import numpy as np
from pathlib import Path

from package.transformers import DocumentToMatrix
from package.estimators import CorrelationEstimator
from package.splitters import SingleThresholdSplitter


class SplitTextTask(luigi.Task):

  input_file = luigi.Parameter('input-file')

  def output(self):
    path = Path(self.input_file)
    expected_output_file = r'{}/{}_splits.json'.format(path.parent, path.stem)
    return luigi.LocalTarget(expected_output_file)


  def run(self):
    document = ''
    with open(self.input_file, 'r') as input_document:
      document = input_document.read()

    document_transformer = DocumentToMatrix.BasicDocumentToMatrix(document)
    estimator = CorrelationEstimator(document_transformer)
    y = np.array(estimator.evaluate()).flatten().tolist()

    splitter = SingleThresholdSplitter(y, .35)
    sections = splitter.split_document(document_transformer.lines_in_document)
    output_contents = json.dumps(
      { i: section for i, section in enumerate(sections) },
      sort_keys=True
    )

    with self.output().open('w') as outfile:
      outfile.write(output_contents)

if __name__ == '__main__':
  luigi.run()
