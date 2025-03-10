# NLP Introduction

### Roadmap of NLP
1. We use `python` for NLP as a programming language.
2. Text pre-processing Step 1: **Cleaning the text data**
   1. **Tokenization**: This is the process of breaking a stream of text up into words, phrases, symbols, or other meaningful elements.
   2. **Lemmatization**: Lemmatization is the process of grouping together the inflected forms of a word so they can be analyzed as a single item, identified by the word's lemma, or dictionary form.
   3. **Stemming**: Stemming is the process of reducing inflected (or sometimes derived) words to their word stem, base or root form—generally a written word form.
   4. **Stop words removal**: Stop words are the most common words in a language like “the”, “is”, “in”, “for”, “where”, “when”, “to”, “at” etc. These words do not carry important meaning and are usually removed from texts.
3. Text pre-processing Step 2: **Text normalization** Convert text data into numerical data / vectors
   1. **Vectorization**: Vectorization is the process of converting text data into numerical data. This is done by converting text data into a matrix of token counts.
      1. **TF-IDF**: TF-IDF stands for Term Frequency-Inverse Document Frequency. It is a numerical statistic intended to reflect how important a word is to a document in a collection or corpus.
      2. **Bag of Words**: A bag-of-words model, or BoW for short, is a way of extracting features from text for use in modeling, such as with machine learning algorithms.
      3. **Uni-gram**, **Bi-gram**, **N-gram**: N-grams of texts are extensively used in text mining and natural language processing tasks. They are basically a set of co-occurring words within a given window, and when computing the n-grams, you typically move one word forward.
      4. **Word Embedding**: Word embeddings are a type of word representation that allows words with similar meaning to have a similar representation.
4. Text pre-processing Step 3: **Advanced Text normalization** Convert text data into numerical data / vectors 
   1. **Word2Vec**: Word2Vec is a group of related models that are used to produce word embeddings. These models are shallow, two-layer neural networks that are trained to reconstruct linguistic contexts of words.
   2. **Average Word2Vec**: Average Word2Vec is a technique to convert a sentence into vectors. It is done by taking the average of the vectors of the words present in the sentence.
5. Deep Learning for NLP
   1. **RNN**: Recurrent Neural Networks (RNN) are a class of artificial neural networks that are designed to recognize patterns in sequences of data, such as text, genomes, handwriting, the spoken word, numerical times series data, etc.
   2. **LSTM**: Long Short-Term Memory (LSTM) networks are a type of recurrent neural network capable of learning order dependence in sequence prediction problems.
   3. **GRU**: Gated Recurrent Unit (GRU) is a gating mechanism in recurrent neural networks, introduced in 2014 by Kyunghyun Cho et al. The GRU is like a long short-term memory (LSTM) with a forget gate but has fewer parameters than LSTM, as it lacks an output gate.
   4. **Attention Mechanism**: An attention mechanism is a part of a neural network that helps the network to focus on the most relevant parts of the input data, and ignore the irrelevant parts.
6. Text pre-processing Step 4:
   1. **Word Embedding**: Word embeddings are a type of word representation that allows words with similar meaning to have a similar representation.
7. Text pre-processing Step 5:
   1. **Transformer**: The Transformer is a deep learning model introduced in 2017, used primarily in the field of natural language processing (NLP).
8. Text pre-processing Step 6:
   1. **BERT**: BERT (Bidirectional Encoder Representations from Transformers) is a transformer-based machine learning technique for natural language processing (NLP) pre-training developed by Google.
  

## Details
##### Lemmatization 
* **Lemmatization** is a key process in **natural language processing (NLP)** that transforms words to their base or root form (lemma), taking into account the context. 
* It helps in understanding the meaning and structure of words in sentences, which is useful for various NLP tasks.
* Here are some examples to illustrate lemmatization:
* **Verbs:**
  * Original Sentence: "The cats were running in the garden."
  * After Lemmatization: "The cat be run in the garden."
  * In this example:
    - "cats" becomes "cat"
    - "were" becomes "be"
    - "running" becomes "run"
* **Nouns:**
  * Original Sentence: "The children have various toys."
  * After Lemmatization: "The child have various toy."
  * In this example:
    - "children" becomes "child"
    - "toys" becomes "toy"
* **Adjectives:**
  * Original Sentence: "She was happier than her sister."
  * After Lemmatization: "She be happy than her sister."
  * In this example:
    - "happier" becomes "happy"
    - "was" becomes "be"
* Lemmatization considers the context and part of speech of words, which makes it more accurate than stemming (a simpler process that removes affixes from words).

##### Stemming
* Stemming is a technique in natural language processing (NLP) that reduces words to their root form by removing suffixes and prefixes. 
* Unlike **lemmatization**, which considers the context and converts words to their meaningful base forms, stemming uses simple heuristics to chop off parts of words.
* Stemming helps in standardizing words, which is useful for tasks like text analysis, information retrieval, and search engines. 
* However, it can sometimes produce non-standard or incomplete root forms.
* Here are some examples of stemming:
* **Verbs:**
   - "running" becomes "run"
   - "runner" becomes "run"
   - "ran" becomes "ran"
* **Nouns:**
   - "cars" becomes "car"
   - "riding" becomes "ride"
   - "bikes" becomes "bike"
* **Adjectives:**
   - "happiest" becomes "happi"
   - "easier" becomes "easi"
   - "brightest" becomes "bright"
* Notice that stemming can sometimes produce stems that are not valid words (e.g., "happiest" becomes "happi"). 
  * This is because stemming algorithms, such as the Porter Stemmer, use a set of rules to remove common suffixes and prefixes without considering the word's context.
* While stemming is faster and simpler compared to lemmatization, it may not always produce the most accurate results. Nonetheless, it is widely used in NLP applications where speed and simplicity are prioritized.

#### Tokenization
* Tokenization is a fundamental step in natural language processing (NLP), where a stream of text is divided into meaningful pieces, known as tokens. These tokens can be words, phrases, or even punctuation marks. Let's look at a couple of examples to understand how tokenization works.
* Tokenization is essential for tasks such as text analysis, machine translation, and information retrieval. It helps in understanding the structure of the text, making it easier to process and analyze.

##### Example 1: Word Tokenization
* Consider the sentence: ```"I love visiting new places."```
* Using word tokenization, this sentence is broken down into individual words: ```["I", "love", "visiting", "new", "places", "."]```
* Each word and punctuation mark is treated as a separate token.
##### Example 2: Sentence Tokenization
* Now, let's take a short paragraph: ```"He went to the store. Then he met his friend. They had coffee together."```
* Using sentence tokenization, this paragraph is divided into individual sentences: ```["He went to the store.", "Then he met his friend.", "They had coffee together."]```
* Each sentence is treated as a separate token.
##### Example 3: Subword Tokenization
* In some NLP applications, subword tokenization is used, especially with languages that have complex morphology or in cases where the vocabulary is large. 
* For example:```"unhappiness"```
* Using subword tokenization, this word could be broken down into smaller units:```["un", "happiness"]``` Or even smaller subword units:```["un", "happy", "ness"]```

### Topics
* **Corpus**:
   * A corpus is a comprehensive collection of written or spoken texts utilized for linguistic analysis or research.
   * It can encompass a body of text in a specific language, domain, or genre.
   * Examples of corpora include a single paragraph, an entire book, a collection of articles, or a set of tweets.
* **Document**:
   * A document represents a single unit of text within a corpus.
   * It can be as brief as a sentence, a paragraph, or as extensive as an article or any other form of text.
* **Vocabulary**:
   * Vocabulary denotes the set of unique words found within a corpus or document.
   * It is employed to analyze the language, structure, and content of textual data.
* **Words**:
   * Words are the fundamental building blocks of language that convey meaning.
   * They can be combined to form sentences, paragraphs, and more extensive pieces of text.