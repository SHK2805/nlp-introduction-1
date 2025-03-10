from nltk.stem import PorterStemmer, RegexpStemmer, SnowballStemmer

class Stemming:
    def __init__(self):
        self.class_name = self.__class__.__name__
        pass

    def stem_word(self, word):
        tag: str = f"[{self.class_name}]::[stem_word]::"
        stemmer = PorterStemmer()
        return stemmer.stem(word)

    def stem_words(self, words):
        tag: str = f"[{self.class_name}]::[stem_words]::"
        stemmer = PorterStemmer()
        stemmed_words = [stemmer.stem(word) for word in words]
        return stemmed_words

    def stem_word_regex(self, stem_regex, stem_min, stem_word):
        """
        :param stem_regex: The regular expression to use for stemming
        :param stem_min: The minimum length of the word to be stemmed
        :param stem_word: The word to be stemmed
        :return: The stemmed words
        """
        tag: str = f"[{self.class_name}]::[stem_word_regex]::"
        stemmer = RegexpStemmer(stem_regex, min=stem_min)
        return stemmer.stem(stem_word)

    def stem_words_regex(self, stem_regex, stem_min, stem_words):
        """
        :param stem_regex: The regular expression to use for stemming
        :param stem_min: The minimum length of the word to be stemmed
        :param stem_words: The words to be stemmed
        :return: The stemmed words
        """
        tag: str = f"[{self.class_name}]::[stem_words_regex]::"
        stemmer = RegexpStemmer(stem_regex, min=stem_min)
        stemmed_words = [stemmer.stem(word) for word in stem_words]
        return stemmed_words

    def stem_word_snowball(self, stem_word, language="english"):
        """
        :param language: The language to use for stemming
        :param stem_word: The word to be stemmed
        :return: The stemmed words
        """
        tag: str = f"[{self.class_name}]::[stem_word_snowball]::"
        stemmer = SnowballStemmer(language)
        return stemmer.stem(stem_word)

    def stem_words_snowball(self, stem_words, language="english"):
        """
        :param language: The language to use for stemming
        :param stem_words: The words to be stemmed
        :return: The stemmed words
        """
        tag: str = f"[{self.class_name}]::[stem_words_snowball]::"
        stemmer = SnowballStemmer(language)
        stemmed_words = [stemmer.stem(word) for word in stem_words]
        return stemmed_words

