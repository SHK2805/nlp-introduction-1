from nltk import TreebankWordTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize, treebank


# **Order**: Corpus → Document → Paragraph → Sentence → Word
class Tokenization:
    def __init__(self):
        self.class_name = self.__class__.__name__
        pass

    # this will tokenize sentences based on punctuations
    def sent_tokenize(self, data_input):
        tag: str = f"[{self.class_name}]::[sent_tokenize]::"
        return sent_tokenize(data_input)

    # this will tokenize words based on spaces
    def word_tokenize(self, data_input):
        tag: str = f"[{self.class_name}]::[word_tokenize]::"
        return word_tokenize(data_input)

    # this will tokenize words based on punctuations
    def wordpunct_tokenize(self, data_input):
        tag: str = f"[{self.class_name}]::[wordpunct_tokenize]::"
        return wordpunct_tokenize(data_input)

    # this will tokenize words based on treebank
    def treebank_tokenize(self, data_input):
        tag: str = f"[{self.class_name}]::[treebank_tokenize]::"
        return TreebankWordTokenizer().tokenize(data_input)