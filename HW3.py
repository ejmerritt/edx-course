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

file = "hamlets.csv"
hamlets = pd.read_csv(file, index_col=0)
print(len(hamlets))
language, text = hamlets.iloc[0]
data = pd.DataFrame(columns = ["word","count"])
    
