#%%

import pandas as pd
import numpy as np
import re
import time
import matplotlib.pyplot as plt
    
#The first dataframe contains all contractions
df = pd.read_csv("../COSC320Proj/contractions.csv")
#If you would like to test with your own dataset, please change the file below
df2 = pd.read_csv('../COSC320Proj/twitterfull.csv')

#Converts the tweets to a string array
tweets = df2.to_numpy()
tweets = tweets.astype(str)

#Creates an array of definitions 
meaning = df.loc[:,"Meaning"].to_numpy()

#Creates an array of contractions and abbreviations
contraction= df.loc[:,"Contraction"].to_numpy()

#The code below is used to test different batch sizes to create a graph
batch_sizes = [10, 100, 1000, 10000, 100000, len(tweets)]
execution_times = []
#This is used for the O(nm) graph
execution_times2=[]

# Run only this for the actual algorithm

for batch_size in batch_sizes:
    tweets_subset = tweets[:batch_size]
    start_time = time.time()
    for tweet in tweets_subset:
        for i in range(len(contraction)):
            #Checks for punctuation after the word.
            pattern = r"(?i)\b" + contraction[i] + r"(?=[\s'’“”.,!?])"
            tweet[0] = re.sub(pattern, meaning[i], tweet[0])
    end_time = time.time()
    execution_time2 = end_time - start_time
    execution_times2.append(execution_time2)

# The Commented Code Below was used to make the O(nm) line
#for batch_size in batch_sizes:
#    tweets_subset = tweets[:batch_size]
#    start_time = time.time()
#    for tweet in tweets_subset:
#        for i in range(len(contraction)):
#            pattern = r"(?i)\b" + contraction[1] + r"(?=[\s'’“”.,!?])"
#            tweet[0] = re.sub(pattern, meaning[1], tweet[0])
#    end_time = time.time()
#    execution_time2 = end_time - start_time
#    execution_times2.append(execution_time2)

plt.plot(batch_sizes, execution_times2, label='Actual')
#The code below was used to make the O(nm) plot on the graph
#plt.plot(batch_sizes, execution_times2, label='O(nm)')

plt.title('Execution Time vs Number of Entries')
plt.xlabel('Number of Entries (tweets)')
plt.ylabel('Execution Time (seconds)')
plt.legend()
plt.show()


# %%
