corpus = """Project Gutenberg EBooks, Google Books Ngrams, and arXiv Bulk Data Access. There are many text corpora from newswire. Random's"""
# Words by type
inflected_forms = ["playing", "played", "plays", "player", "running", "runner", "runs", "walked", "walking"]
plurals = ["cats", "dogs", "boxes", "flies", "babies", "leaves", "wolves"]
prefixes = ["undo", "undone", "unlikely", "disconnected", "misaligned", "pretest"]
suffixes = ["happiness", "quickly", "carefulness", "nationalization", "arguing", "organization"]
derived_words = ["enjoying", "enjoyment", "beautiful", "beautify", "beautifully"]
irregulars = ["went", "gone", "goes", "better", "best", "children", "feet", "mice"]
others = ["History", "eat", "ate", "eaten", "eats", "eating",
               "History", "historical", "historically", "historian",
               "historians", "histories", "history", "history's", "unhistorical", "unhistorically", "Congratulation"
               ]

# Final list
all_words = inflected_forms + plurals + prefixes + suffixes + derived_words + irregulars + others

# stemming
stemming_regex = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
stemming_min = 4
