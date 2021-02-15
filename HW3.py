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
