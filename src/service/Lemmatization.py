from nltk.stem import WordNetLemmatizer


class Lemmatization:
    def __init__(self):
        self.class_name = self.__class__.__name__
        pass

    # this will lemmatize words
    # Here pos is the part of speech of the word
    def lemmatize(self, data_input, pos):
        tag: str = f"[{self.class_name}]::[lemmatize]::"
        lemmatizer = WordNetLemmatizer()
        return lemmatizer.lemmatize(data_input, pos)

    # this will lemmatize multiple words
    # Here pos is the part of speech of the word
    def lemmatize_words(self, data_input, pos):
        tag: str = f"[{self.class_name}]::[lemmatize_words]::"
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(word, pos) for word in data_input]