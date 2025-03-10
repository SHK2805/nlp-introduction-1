from antlr4.tree.Trees import Trees
from nltk import TreebankWordTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize, treebank


# **Order**: Corpus → Document → Paragraph → Sentence → Word
class Tokenization:
    def __init__(self):
        self.class_name = self.__class__.__name__
        pass

    # this will tokenize sentences based on punctuations
    def sent_tokenize(self, input):
        tag: str = f"[{self.class_name}]::[sent_tokenize]::"
        return sent_tokenize(input)

    # this will tokenize words based on spaces
    def word_tokenize(self, input):
        tag: str = f"[{self.class_name}]::[word_tokenize]::"
        return word_tokenize(input)

    # this will tokenize words based on punctuations
    def wordpunct_tokenize(self, input):
        tag: str = f"[{self.class_name}]::[wordpunct_tokenize]::"
        return wordpunct_tokenize(input)

    # this will tokenize words based on treebank
    def treebank_tokenize(self, input):
        tag: str = f"[{self.class_name}]::[treebank_tokenize]::"
        return TreebankWordTokenizer().tokenize(input)