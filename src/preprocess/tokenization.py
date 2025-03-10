from src.constants import *
from src.service.Tokenization import Tokenization
from src.utils.utils import print_line

print(corpus)

# tokenization
tokenizer = Tokenization()
# corpus -> documents
documents = tokenizer.sent_tokenize(corpus)
print_line()
print("Printing documents")
print(documents)
print_line()

# print sentences from documents
print_line()
print("Printing sentences from documents")
for sent in documents:
    print(sent)
print_line()

# corpus -> words
# sentence -> words
words = tokenizer.word_tokenize(corpus)
print_line()
print("Printing words from corpus")
print(words)
print_line()

# print words from sentences
print_line()
print("Printing words from sentences")
for sent in documents:
    words = tokenizer.word_tokenize(sent)
    print(words)
print_line()

# corpus -> words using punctuations
print_line()
print("Printing words from corpus using punctuations")
words = tokenizer.wordpunct_tokenize(corpus)
print(words)
print_line()

# corpus -> words using treebank
print_line()
print("Printing words from corpus using treebank")
words = tokenizer.treebank_tokenize(corpus)
print(words)
print_line()