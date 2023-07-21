
""" 
  This script will read the text corups(file location mentioned in filepath.txt file) 
  and create a dictonary with word frequency  . 
"""
##---------------------------------------------------------------------
# importing modules that we are going to need 
## ---------------------------------------------------------------------
import nltk
from nltk.tokenize import word_tokenize
import json 
import re

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('words') 
### ------------------------ Helper functions --------------------------
def is_valid_word(word):
    # Regular expression pattern to match valid words
    pattern = r"^[a-zA-Z0-9\-']+$"
    return re.match(pattern, word) is not None
## ---------------------------------------------------------------------



## ---------------------------------------------------------------------
##  Reading the Input file which we need to correct (file location is mentioned in filepath.txt)
## ---------------------------------------------------------------------
with open("filepath.txt", 'r') as file:
    file_path = file.read()
try:    
    ## Reading the File here 
    with open(file_path, 'r') as file:
        content = file.read()
    ## Converting into tokens (words).NOTE: word_tokenize is more efficient that spliting with whitespaces 
    tokens = word_tokenize(content)
    word_frequency = {}

    for token in tokens:
        if token=="END-OF-CORPUS":
            break           
        if is_valid_word(token):
            if token not in word_frequency:
                word_frequency[token] = 1
            else:
                word_frequency[token] = +1 
    
    #storing the word frequency dictonary as json file for future use 
    with open('word_frequency.json', 'w') as file2:
        json.dump(word_frequency, file2)

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except IOError:
    print(f"Error reading file '{file_path}'.")
