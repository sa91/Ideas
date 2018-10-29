from Spellscore import score
from nltk.corpus import words


def embed(word):
    """
     return similarity encoding across the vocabulary
    """
    word_array = words.words()
    embedding = [0]*len(word_array)
    for i in range(len(word_array)):
        embedding[i] = score(word, word_array[i])
    return embedding

