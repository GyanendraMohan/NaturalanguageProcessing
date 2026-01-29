## Natural Language Processing – Lab 1

### Overview

This repository contains introductory experiments in **Natural Language Processing (NLP)** using Python and NLTK. The notebook `notebooks/lab1.ipynb` walks through basic text processing steps and core lexical semantics concepts.

### Theory from `notebooks/lab1.ipynb`

- **NLTK resources**
  - NLTK (Natural Language Toolkit) provides corpora and tools for NLP.
  - The notebook configures `nltk_data` locally and ensures key resources are available:
    - **`punkt`**: pre-trained models for sentence and word tokenization.
    - **`stopwords`**: lists of common words (like “the”, “is”, “and”) that often carry little semantic content.
    - **`wordnet`** and **`omw-1.4`**: lexical database of English words and multilingual wordnets.

- **Tokenization**
  - **Sentence tokenization (`sent_tokenize`)**:
    - Splits raw text into sentences based on punctuation and learned patterns.
    - This is often the first step in NLP pipelines because many tasks operate at the sentence level (e.g., sentiment analysis, translation).
  - **Word tokenization (`word_tokenize`)**:
    - Splits a sentence or text into individual tokens (usually words and punctuation).
    - Important for tasks like frequency analysis, language modeling, and downstream feature extraction.
  - **Regular expression tokenization (`RegexpTokenizer`)**:
    - Uses a custom regular expression (here `\w+`) to define what counts as a token.
    - `\w+` matches sequences of alphanumeric characters, effectively removing punctuation and giving cleaner word tokens.
    - Regex-based tokenization is useful when we need strict control over token boundaries.

- **Stopword removal**
  - **Stopwords** are very frequent function words (e.g., “the”, “is”, “to”) that often do not contribute much to the main meaning of a text in tasks like topic modeling or keyword extraction.
  - The notebook:
    - Loads English stopwords from NLTK.
    - Filters out any word in the token list that appears in the stopword set.
  - Removing stopwords:
    - Reduces noise and vocabulary size.
    - Can improve performance for some models, though for modern deep models it is sometimes skipped depending on the task.

- **WordNet and Synsets**
  - **WordNet** is a large lexical database where:
    - Words are grouped into sets of cognitive synonyms called **synsets**.
    - Each synset represents a distinct sense (meaning) of a word and is associated with a definition and usage examples.
  - In the notebook:
    - The user enters a word `word1`.
    - `wordnet.synsets(word1)` retrieves all synsets (senses) for that word.
    - Each synset has:
      - A unique name (e.g., `welcome.n.01` where the suffix indicates part of speech and sense number).
      - A **definition** that explains that sense of the word.
  - Synsets provide the basis for many semantic similarity and word-sense disambiguation methods.

- **Lemmas**
  - Within WordNet, each synset contains one or more **lemmas**:
    - A lemma is a canonical form of a word (e.g., “run” for “runs”, “running”).
    - Lemmas correspond to word forms that can appear in text.
  - The notebook:
    - Iterates over all synsets for `word1`.
    - Collects their lemma names into a set to show different surface forms tied to the same or related senses.

- **Semantic similarity**
  - **Semantic similarity** measures how close in meaning two words (or synsets) are.
  - The notebook:
    - Takes a second word `word2`.
    - Retrieves synsets for both `word1` and `word2`.
    - Uses `path_similarity` on the first synset of each:
      - `path_similarity` is based on the length of the path between two synsets in the WordNet **hypernym/hyponym** (is-a) hierarchy.
      - A shorter path implies higher similarity (values range from 0 to 1, where 1 means identical synsets).
  - Such similarity measures are used in tasks like word sense disambiguation, information retrieval, and ontology-based reasoning.

- **Collocations**
  - **Collocations** are word pairs or sequences that occur together more often than would be expected by chance (e.g., “strong tea”, “natural language”).
  - The notebook:
    - Uses `BigramCollocationFinder` to find frequent **bigrams** (two-word sequences) in the filtered tokens (after stopword removal).
    - Ranks bigrams using **likelihood ratio**, a statistical association measure that compares observed co-occurrence to what would be expected if the words were independent.
    - Displays the top bigram collocations.
  - Collocation extraction helps in:
    - Discovering multi-word expressions.
    - Improving language modeling.
    - Identifying phrase-level features in texts.

### Summary

In summary, `lab1.ipynb` introduces a classic NLP preprocessing pipeline:

- Converting raw text into sentences and tokens.
- Cleaning tokens by removing stopwords and punctuation.
- Exploring lexical semantics with WordNet: synsets, lemmas, and semantic similarity.
- Identifying statistically significant word pairings (collocations).

These concepts form the theoretical foundation for more advanced NLP tasks such as text classification, information extraction, and semantic analysis.

