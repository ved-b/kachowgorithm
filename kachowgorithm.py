#%%
# The Kachowgarithm 
# Created by Ved Ballary, Aaron Deo, Noah Stasuik
# Created on Apr 3, 2023
# V1.0.0

#-------------------- IMPORTS --------------------------------------------------
import pandas as pd
import numpy as np
import re
import time
import matplotlib.pyplot as plt
import string

#-------------------BORING STUFF LIKE IMPORTING DATA--------------------------

wordDict = {}
wordDict2 = {}
#The first dataframe contains all contractions
df = pd.read_csv("../COSC320Proj/contractions.csv")
#If you would like to test with your own dataset, please change the file below
df2 = pd.read_csv('../COSC320Proj/twitterfull.csv')

#Converts the tweets to a string array for Kachowgarithm
tweets = df2.to_numpy()
tweets = np.array([tweet[0] for tweet in tweets])
tweets = tweets.astype(str)

#Creates an array of definitions 
meaning = df.loc[:,"Meaning"].to_numpy()

#Creates an array of contractions and abbreviations
contraction= df.loc[:,"Contraction"].to_numpy()

batch_sizes = [10, 100, 1000, 10000, 100000, len(tweets)]
execution_times = []
#Used to store O(n+m) version values
#execution_times2=[]

#--------------------- LICENSE PLATING --------------------------------------

#This is the licensePlating method which creates a unique key for every word
def licensePlating(a):
    out = 0

    for i in range(1, len(a)+1):
        out += ord(a[i-1]) * (10 ** (len(a)-i))

    return out
# We create the hashmap
for i in range(len((contraction))):
    wordDict[licensePlating(contraction[i])] = meaning[i]
#print(wordDict)
# Create a one word hashmap for creating the O(n+m) algorithm
# wordDict2[licensePlating(contraction[1])] = meaning[1]
#----------------------- THE ALGORITHM -------------------------------
# This is the kachowgorithm  - RUN THIS ONLY FOR THE ACTUAL ALGORITHM
for batch_size in batch_sizes:
    tweets_subset = tweets[:batch_size]
    start_time = time.time()
    for tweet in tweets_subset:
        words = tweet.split()
        
        for i, word in enumerate(words):
            word = word.lower()
            word = word.strip(string.punctuation)
            word_hash = licensePlating(word)
            
            if word_hash in wordDict:
                words[i] = wordDict[word_hash]
        
        modified_tweet = " ".join(words)
        print(modified_tweet)
    end_time = time.time()
    execution_time = end_time - start_time
    execution_times.append(execution_time)

# This is the kachowgarithm but simplified for getting pure O(n+m)
#for batch_size in batch_sizes:
#    tweets_subset = tweets[:batch_size]
#    start_time = time.time()
#    for tweet in tweets_subset:
#        words = tweet.split()
#        
#        for i, word in enumerate(words):
#            word = word.lower()
#            word = word.strip(string.punctuation)
#            word_hash = licensePlating(word)
#            
#            if word_hash in wordDict2:
#                words[i] = wordDict2[word_hash]
#        
#        modified_tweet = " ".join(words)
#        print(modified_tweet)
#    end_time = time.time()
#    execution_time2 = end_time - start_time
#    execution_times2.append(execution_time2)

#-----------------GRAPHS THE RUNTIME----------------------------
 
plt.plot(batch_sizes, execution_times, label='Kachowgarithm')
#plt.plot(batch_sizes, execution_times2, label='O(n+m)')
plt.title('Execution Time vs Number of Entries')
plt.xlabel('Number of Entries (tweets)')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.show()
plt.show()
#%%
