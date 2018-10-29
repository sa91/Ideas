from Preprocess import pre_process
from Getembedding import embed
from Predictor import predictor
"""
    Input of this file can be changed to stream word or anything that can be used to check spelling
    For now:
        It takes a word, preprocess it 
        get embedding  of the word
        send it to predictor
    Ideas:
        Take a stream around the word, preprocess each word.
        get embedding each word
        send the stream encoding to predictor       
        
"""
word = input("Input the spelling: ")
word = pre_process(word)
k = input("Number of suggestion: ")
embedding = embed(word)
print("Suggestions: ", predictor(embedding, int(k)))


