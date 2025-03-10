from nltk import pos_tag

# Parts of Speech (POS) Tagging
class PartsOFSpeechTagging:
    def __init__(self):
        self.class_name = self.__class__.__name__

    def tag(self, data_input):
        tag: str = f"[{self.class_name}]::[tag]::"
        # pos_tag takes a list of words and returns a list of tuples
        return pos_tag(data_input)

    def tag_str(self, data_input: str):
        tag: str = f"[{self.class_name}]::[tag_str]::"
        # it the input is a string, split the string into a list of words
        return pos_tag(data_input.split())
