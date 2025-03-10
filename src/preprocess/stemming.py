from src.constants import all_words
from src.service.Stemming import Stemming
from src.utils.utils import print_line

stemmer = Stemming()
print_line()
print("Stemming words")
stemmed_words = stemmer.stem_words(all_words)
print(all_words)
print(stemmed_words)
print_line()

print_line()
print("Stemming words")
stemmed_word = stemmer.stem_word("History")
print(f"History: {stemmed_word}")
print_line()

print_line()
print("Stemming words")
stemmed_word = stemmer.stem_word("Conversation")
print(f"Conversation: {stemmed_word}")
print_line()

print_line()
print("Stemming words using Snowball")
stemmed_word = stemmer.stem_word("fairly")
print(f"fairly: {stemmed_word}")
print_line()

print_line()
print("Stemming words using Snowball")
stemmed_word = stemmer.stem_word("sportingly")
print(f"sportingly: {stemmed_word}")
print_line()

print_line()
print("Stemming words using regex")
stemmed_word = stemmer.stem_word_regex(r"ing$", 3, "History")
print(f"History: {stemmed_word}")
print_line()

print_line()
print("Stemming words using regex")
stemmed_word = stemmer.stem_word_regex(r"ing$", 3, "Eating")
print(f"Eating: {stemmed_word}")
print_line()

print_line()
print("Stemming words using regex")
stemmed_word = stemmer.stem_word_regex(r"ing$", 3, "IngEating")
print(f"IngEating: {stemmed_word}")
print_line()

print_line()
print("Stemming words using Snowball")
stemmed_word = stemmer.stem_word_snowball("fairly")
print(f"History: {stemmed_word}")
print_line()

print_line()
print("Stemming words using Snowball")
stemmed_word = stemmer.stem_word_snowball("fairly")
print(f"fairly: {stemmed_word}")
print_line()

print_line()
print("Stemming words using Snowball")
stemmed_word = stemmer.stem_word_snowball("sportingly")
print(f"sportingly: {stemmed_word}")
print_line()

print_line()
temp_words = ["History", "Conversation", "fairly", "sportingly", "goes", "flies"]
for word in temp_words:
    snowball_stemmed_word = stemmer.stem_word_snowball(word)
    stemmed_word = stemmer.stem_word(word)
    print(f"{word}: {stemmed_word} - {snowball_stemmed_word}")
print_line()