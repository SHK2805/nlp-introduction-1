from src.constants import all_words
from src.service.Lemmatization import Lemmatization
from src.utils.parts_of_speech import PartOfSpeech
from src.utils.utils import print_line

lemmatizer = Lemmatization()
print_line()
lem_word = "going"
print(f"{lem_word} --> {lemmatizer.lemmatize(lem_word, PartOfSpeech.VERB.value)}")
print_line()

print_line()
lem_word = "goes"
print(f"{lem_word} --> {lemmatizer.lemmatize(lem_word, PartOfSpeech.VERB.value)}")
print_line()

print_line()
for word in all_words:
    print(f"{word} --> {lemmatizer.lemmatize(word, PartOfSpeech.VERB.value)}")