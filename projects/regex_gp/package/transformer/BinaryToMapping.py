class BinaryToMapping:
    
    mapping = {}
    
    def __init__(self, mapping):
        self.mapping = mapping
        
    def transform(self, binary_string):
        return self.mapping[binary_string]

    def transform_array(self, binary_array):
        return [ self.transform(binary_string) for binary_string in binary_array ]
