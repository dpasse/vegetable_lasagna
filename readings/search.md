
# "Search" Readings

#### Title: "How to Build A Vertical Search Engine Using Python?"
#### URI: https://elhamamini.medium.com/how-to-build-a-vertical-search-engine-using-python-f09b137b5db
#### Github: https://github.com/lhamini/Search_Engine_medium
#### Points:
- Generialized search engine, which focuses on many subjects, is not always the most efficent.
- Vertical search engine focuses on one subject.
- Post focused on airline crash dataset. Build out a simple vertical search engine.
- Packages: nltk, rank-bm25
- Preprocessing: lower case, tokenize terms, remove stop words, porter stem
- bm25 = TF (Term Frequency) * IDF (Inverse Document Frequency) * QTF (Query Term Frequency)

#### Query:
```
corpus = [
  '', -- row is a document
]

tokenized_corpus = [
  [...], -- row contains cleaned, tokenized, stemmed terms per document
]

tokenized_query = ['hijack', 'survivor']
BM25Okapi(tokenized_corpus).get_top_n(tokenized_query, corpus, n=5)
```

<hr/>