import gensim
from gensim.models import Word2Vec, KeyedVectors
import gensim.downloader as api

class Word2VecService:
    def __init__(self, model_name:str = 'word2vec-google-news-300'):
        self.class_name = self.__class__.__name__
        self.model_name = model_name
        self.model = api.load(model_name)

    def get_similarity(self, word1, word2):
        return self.model.similarity(word1, word2)

    def get_most_similar(self, word):
        return self.model.most_similar(word)

    def get_vector(self, word):
        return self.model[word]

    def get_model(self):
        return self.model

    def get_model_name(self):
        return self.model_name

