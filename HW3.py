#---------DNA TRANSLATION--------------#
# Exercise 1
import string
#The string library has been imported. Create a string called alphabet consisting of the space character ' ' followed
#by (concatenated with) the lowercase letters. Note that we're only using the lowercase letters in this exercise.
alphabet = " " + string.ascii_lowercase

# Exercise 2
#alphabet has already been defined in the last exercise. Create a dictionary with keys consisting of the characters in
#alphabet and values consisting of the numbers from 0 to 26.
#Store this as positions.
positions = {}
for letter in alphabet:
    positions[letter] = alphabet.index(letter)

# Exercise 3
#alphabet and positions have already been defined in previous exercises. Use positions to create an encoded message based
#on message where each character in message has been shifted forward by 1 position, as defined by positions.
#Note that you can ensure the result remains within 0-26 using result % 27
#Store this as encoded_message.
message = "hi my name is caesar"
def caesar(message, key):
    alphabet_len = len(alphabet)
    encoded_message = {alphabet[i]:((i + key) % alphabet_len) for i in range(alphabet_len)}
    return ''.join([alphabet[encoded_message[letter]] for letter in message])
encoded_message = caesar(message, 1)
print(encoded_message)

# Exercise 4
# Make the key = 3
encoded_message = caesar(message, 3)
print(encoded_message)

#---------LANGUAGE PROCESSING--------------#
import os
import pandas as pd
import numpy as np
from collections import Counter

def count_words_fast(text):
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"', "\n", "!", "?", "(", ")"]
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts

def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })

    data.loc[data["count"] > 10,  "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1,  "frequency"] = "unique"

    data["length"] = data["word"].apply(len)

    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent","infrequent","unique"],
        "mean_word_length": data.groupby(by = "frequency")["length"].mean(),
        "num_words": data.groupby(by = "frequency").size()
    })

    return(sub_data)

# Exercise 1
#Read in the data as a pandas dataframe using pd.read_csv. Use the index_col argument to set the first column in
#the csv file as the index for the dataframe.
file = "hamlets.csv"
hamlets = pd.read_csv(file, index_col=0)
print(len(hamlets))

# Exercise 2
#Find the dictionary of word frequency in text by calling count_words_fast(). Store this as counted_text.
#Create a pandas dataframe named data.
#Using counted_text, define two columns in data:
    #word, consisting of each unique word in text.
    #count, consisting of the number of times each word in word is included in the text.
language, text = hamlets.iloc[0]
counted_text = dict(count_words_fast(text))
print(counted_text["hamlet"])
data = pd.DataFrame.from_dict(counted_text, orient="index").reset_index()
data = data.rename(columns = {"index":"word", 0:"count"})

# Exercise 3
#Add a column to data named length, defined as the length of each word.
#Add another column named frequency, which is defined as follows for each word in data:
#    If count > 10, frequency is "frequent".
#    If 1 < count <= 10, frequency is "infrequent".
#    If count == 1, frequency is "unique".
data["length"] = data["word"].apply(len)
data.loc[data["count"] > 10,  "frequency"] = "frequent"
data.loc[data["count"] <= 10, "frequency"] = "infrequent"
data.loc[data["count"] == 1,  "frequency"] = "unique"
print(data.head)
print(data.frequency.value_counts().unique)

# Exercise 4
#Create a pandas dataframe named sub_data including the following columns:
#    language, which is the language of the text (defined in Exercise 2).
#    frequency, which is a list containing the strings "frequent", "infrequent", and "unique".
#    mean_word_length, which is the mean word length of each value in frequency.
#    num_words, which is the total number of words in each frequency category.
import statistics
sub_data = pd.DataFrame(columns = ["language", "frequency", "mean_word_length", "num_words"])
sub_data.loc[1] = language,  ["frequent", "infrequent", "unique"], [(data.loc[data["frequency"] == "frequent", statistics.mean(data[length])]),(data.loc[data["frequency"] == "infrequent", statistics.mean(data["length"])]),(data.loc[data["frequency"] == "unique", statistics.mean(data["length"])])], [(sum(data.loc[data["frequency"] == "frequent"])), (sum(data.loc[data["frequency"] == "infrequent"])), (sum(data.loc[data["frequency"] == "unique"]))]
sub_data.head()

# Exercise 5
#The previous code for summarizing a particular translation of Hamlet is consolidated into a single function called summarize_text.
#Create a pandas dataframe grouped_data consisting of the results of summarize_text for each translation of Hamlet in hamlets.
#    Use a for loop across the row indices of hamlets to assign each translation to a new row.
#    Obtain the ith row of hamlets to variables using the .iloc method, and assign the output to variables language and text.
#    Call summarize_text using language and text, and assign the output to sub_data.
#    Use the pandas .append() function to append to pandas dataframes row-wise to grouped_data.


# Exercise 6
#Plot the word statistics of each translations on a single plot. Note that we have already done most of the work for you.
#Consider: do the word statistics differ by translation?


#---------CLASSIFICATION--------------#
import numpy as np, random, scipy.stats as ss

def majority_vote_fast(votes):
    mode, count = ss.mstats.mode(votes)
    return mode

def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]

def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote_fast(outcomes[ind])[0]

# Exercise 1
#Import dataset
import pandas as pd
dataset = pd.read_csv("wine.csv")
#Taking a look at the first 5 rows of the dataset, how many wines in those 5 rows are considered high quality?
print(dataset.head)

# Exercise 2
#In order to get all numeric data, we will change the color column to an is_red column.
#    If color == 'red', we will encode a 1 for is_red
#    If color == 'white', we will encode a 0 for is_red
#Create this new column, is_red.
#Drop the color, quality, and high_quality columns as we will be predict the quality of wine using numeric data in a later exercise
#Store this all numeric data in a pandas dataframe called numeric_data
numeric_data = dataset
numeric_data.loc[numeric_data["color"] == "red",  "is_red"] = 1
numeric_data.loc[numeric_data["color"] == "white",  "is_red"] = 0
numeric_data = numeric_data.drop(labels=["color", "quality", "high_quality"], axis=1)
print(numeric_data.head)
#How many red wines?
print(numeric_data.groupby(by="is_red").agg("count"))

# Exercise 3
#Scale the data using the sklearn.preprocessing function scale() on numeric_data.
#Convert this to a pandas dataframe, and store as numeric_data.
#    Include the numeric variable names using the parameter columns = numeric_data.columns.
#Use the sklearn.decomposition module PCA() and store it as pca.
#Use the fit_transform() function to extract the first two principal components from the data, and store them as principal_components.
#Note: You may get a DataConversionWarning, but you can safely ignore it
import sklearn.preprocessing
scaled_data = sklearn.preprocessing.scale(numeric_data)
numeric_data = pd.DataFrame(scaled_data, columns = numeric_data.columns)

import sklearn.decomposition
pca = sklearn.decomposition.PCA(n_components = 2) # pca stands for principal component analysis
principal_components = pca.fit_transform(numeric_data)



# Exercise 4
# Exercise 5
# Exercise 6
# Exercise 7
# Exercise 8
# Exercise 9
