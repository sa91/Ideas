from nltk.corpus import words
import numpy as np

def predictor(embedded_info,k):
    """
    Ideas:
        Let embedded_info be array of embeddings of stream
        Use an LSTM to predict the words
        Output the predicted word
    Now:
        Output the highest scoring word
    """
    matches = [""]*k
    embedded_info = np.array(embedded_info)
    ind = embedded_info.argsort()[-k:][::-1]
    word_array = words.words()
    for i in range(k):
        matches[i] = word_array[ind[i]]
    return matches