import pickle

from .serializer_abstract import Serializer
class PickleSerializer(Serializer):

    file_ending = ".pickle"
    
    def serialize(self, content: str):
        serialized = pickle.dumps(content)
        return serialized
    def deserialize(self, serialized_content):
        return pickle.loads(serialized_content)
