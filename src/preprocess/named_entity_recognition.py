from src.constants import ner_corpus
from src.service.Tokenization import Tokenization

# get data
data = ner_corpus
# tokenization
tokenization = Tokenization()
words = tokenization.word_tokenize(data)
# print(words)

