from pydantic.v1.utils import to_lower_camel

from src.constants import long_corpus
from src.service.Tokenization import Tokenization
from src.service.Lemmatization import Lemmatization
from src.service.StopWords import StopWords
from src.utils.parts_of_speech import PartOfSpeech

tokenization = Tokenization()
lematizer = Lemmatization()
stop_words = StopWords()
data = long_corpus

# Steps
# 1. Tokenize the data into sentences and tokenize the sentences into words
# 2. Remove stop words
# 3. Stem the words

# Tokenize the data into sentences
sentence = tokenization.sent_tokenize(data)

# Tokenize the sentences into words
for i in range(len(sentence)):
    # Tokenize the sentence into words
    words = tokenization.word_tokenize(sentence[i])
    # Remove stop words
    lem_words = [lematizer.lemmatize(word.lower(),PartOfSpeech.NOUN.value) for word in words if word not in stop_words.get_stop_words("english")]
    # join the stemmed words into a sentence
    sentence[i] = " ".join(lem_words)

print(sentence)
