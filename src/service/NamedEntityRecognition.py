import nltk
from nltk import ne_chunk

class NamedEntityRecognition:
    def __init__(self):
        pass

    def get_named_entities(self, text):
        named_entities = []
        for sentence in nltk.sent_tokenize(text):
            for chunk in ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence))):
                if hasattr(chunk, 'label'):
                    named_entities.append(chunk)
        return named_entities

    def draw_named_entities(self, text):
        ne_chunk(text).draw()