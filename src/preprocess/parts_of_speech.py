from src.constants import long_corpus
from src.service.Tokenization import Tokenization
from src.service.StopWords import StopWords
from src.service.PartsOfSpeechTagging import PartsOFSpeechTagging

data = long_corpus
# Steps
# 1. Tokenize the data into sentences
# 2. Tokenize the data into words
# 3. Remove stop words
# 4. Find the POS of each word in the sentence

# Tokenize the data into sentences
tokenizer = Tokenization()
sentence = tokenizer.sent_tokenize(data)

# Find the POS of each word in the sentence
stop_words = StopWords()
pos = PartsOFSpeechTagging()
print(f"Pos: {pos.tag_str('Hello from Earth which is the third planet from the sun')}")
for sent in sentence:
    word_tokens = tokenizer.word_tokenize(sent)
    # remove stop words
    words = [word for word in word_tokens if word.lower() not in stop_words.get_stop_words("english")]
    pos_tags = pos.tag(words)
    print(pos_tags)
