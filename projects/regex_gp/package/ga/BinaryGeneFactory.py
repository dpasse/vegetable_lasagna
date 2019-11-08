import numpy as np
from ..transformer import IntegerToBinaryString


class BinaryGeneFactory():
    
    transformer = None
    
    def __init__(self, max_length):
        self.transformer = IntegerToBinaryString.IntegerToBinaryString(max_length)
    
    def create(self, start, end):
        random_integer = np.random.randint(start, end)
        return self.transformer.transform(random_integer)
    
    def create_many(self, start, end, total):
        return [ self.create(start, end) for _ in range(total) ]
