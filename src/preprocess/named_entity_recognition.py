from src.constants import ner_corpus
from src.service.Tokenization import Tokenization
from src.service.PartsOfSpeechTagging import PartsOFSpeechTagging
from src.service.NamedEntityRecognition import NamedEntityRecognition

# get data
data = ner_corpus
# tokenization
tokenization = Tokenization()
words = tokenization.word_tokenize(data)
# print(words)
# tag words
pos = PartsOFSpeechTagging()
pos_words = pos.tag(words)
# print(pos_words)
# named entity recognition
named_entities = NamedEntityRecognition()
named_entities = named_entities.draw_named_entities(pos_words)

