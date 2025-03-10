corpus = """Project Gutenberg EBooks, Google Books Ngrams, and arXiv Bulk Data Access. There are many text corpora from newswire. Random's"""
# Words by type
stem_inflected_forms = ["playing", "played", "plays", "player", "running", "runner", "runs", "walked", "walking"]
stem_plurals = ["cats", "dogs", "boxes", "flies", "babies", "leaves", "wolves"]
stem_prefixes = ["undo", "undone", "unlikely", "disconnected", "misaligned", "pretest"]
stem_suffixes = ["happiness", "quickly", "carefulness", "nationalization", "arguing", "organization"]
stem_derived_words = ["enjoying", "enjoyment", "beautiful", "beautify", "beautifully"]
stem_irregulars = ["went", "gone", "goes", "better", "best", "children", "feet", "mice"]
stem_others = ["History", "eat", "ate", "eaten", "eats", "eating",
               "History", "historical", "historically", "historian",
               "historians", "histories", "history", "history's", "unhistorical", "unhistorically", "Congratulation"
               ]

# Final list
stem_all_words = stem_inflected_forms + stem_plurals + stem_prefixes + stem_suffixes + stem_derived_words + stem_irregulars + stem_others

# stemming
stemming_regex = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
stemming_min = 4
