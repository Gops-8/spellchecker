
""" 
  This script will read the word frequency dictonary and check if words are misplelled  
  and create a dictonary with suggestion of correct word if misspelled  . 
"""
##---------------------------------------------------------------------
# importing modules that we are going to need 
## ---------------------------------------------------------------------
import nltk
from nltk.corpus import words
import json 
import re
from tqdm import tqdm

##------------------------ Helper Function------------------------------

##  function to calculate levenshtein distance 
def levenshtein_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        new_distances = [index2 + 1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                new_distances.append(distances[index1])
            else:
                new_distances.append(1 + min((distances[index1], distances[index1 + 1], new_distances[-1])))
        distances = new_distances
    return distances[-1]

##  Get Suggestion based on levenshtein distance 

def suggest_replacement(word, suggestions_count=5):

    word_list = words.words()
    suggestions = []
    for w in word_list:
        if len(w) == len(word) and w[0].islower() and w.isalpha():
            distance = levenshtein_distance(word, w)
            suggestions.append((w, distance))
    suggestions.sort(key=lambda x: x[1])

    return [s[0] for s in suggestions[:suggestions_count]]

##-----------------------------------------------------------------------

## ---------------------------------------------------------------------
##  Reading the wordfrequency  file generated in prev script
## ---------------------------------------------------------------------
with open('word_frequency.json', 'r') as file2:
    json_words=json.loads(file2.read())

tokens = [token for token in json_words]
english_words = set(words.words())

## Check if the word is misspelled or not  (NOTE: this will include Nouns since this is part of english dictonary)
misspelled_tokens = [token for token in tokens if token.lower() not in english_words]

print(f"Out of {len(tokens)} Words there are {len(misspelled_tokens)} mis-spelled words ")

json_output=[]
for word in tqdm(misspelled_tokens):
  
    corrected_word = suggest_replacement(word)
    json_output.append({word:corrected_word})

## saving the suggestions  in a dictonary 
with open('dictonary_of_suggestion.json', 'w') as file:
        json.dump(json_output, file, indent=4)






    