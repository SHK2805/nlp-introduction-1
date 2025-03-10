from nltk.corpus import stopwords

class StopWords:
    def __init__(self):
        self.class_name = self.__class__.__name__

    def get_stop_words(self, language: str="english"):
        tag: str = f"[{self.class_name}]::[get_stop_words]::"
        return stopwords.words(language)