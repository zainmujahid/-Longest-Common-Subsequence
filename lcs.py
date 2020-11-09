#################### Importing Requirements ####################
import spacy
import pandas as pd
import warnings
import os
warnings.filterwarnings('ignore')

nlp = spacy.load("ur_model") # Make sure to Download and Install model from https://github.com/mirfan899/Urdu


################## Longest COmmon Subsequence ##################
def lcs(X, Y, m, n):

    """
    Recurrent implementation for finding LCS between 2 sentences
    X: Tokenized Sentence 1
    Y: Tokenized Sentence 2
    m: length of X
    n: length of Y
    """

    if m == 0 or n == 0:                 # To deal with any redundant new lines
       return 0; 
    elif X[m-1].similarity(Y[n-1]) == 1: # If cosine similarity between two tokens is 1 then they are same.
       return 1 + lcs(X, Y, m-1, n-1); 
    else: 
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)); 


text = open("./data.txt", encoding="utf8").read() # Reading raw text
sentences = text.split("\n") # extracting sentences from the raw text

######### Word Tokenization using SpaCy ########## 
dict = {}
for i in range (0, len(sentences)):
    dict[i] = nlp (sentences[i])
    i += 1


##################  Calculating LCS between Sentencing and storing them into a 2D List #####################
arr2D = [[0 for col in range(len(sentences))] for row in range(len(sentences))] # Initializing list of lists
for row in range (0, len(sentences)):
    for column in range (0, len(sentences)):
        arr2D[row][column]= lcs(dict[row], dict[column], len(dict[row]), len(dict[column]))

########################## Converting List of Lists into a pandas dataframe ################################
df = pd.DataFrame.from_records(arr2D)
print("\n","The Longest Common Subsequences between sentences (ZERO INDEXED) are:" , "\n")
print(df)