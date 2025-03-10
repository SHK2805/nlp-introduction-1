from enum import Enum

class PartOfSpeech(Enum):
    NOUN = "n"
    VERB = "v"
    ADJECTIVE = "a"
    ADVERB = "r"
    SATELLITE_ADJECTIVE = "s"

# Example usage:
# pos = PartOfSpeech.NOUN
# print(pos.value)  # Output: 'n'
