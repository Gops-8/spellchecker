#import modules 

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tqdm import tqdm
# nltk.download('punkt')
# nltk.download('stopwords')  
import enchant
import json 
import enchant
import re

def is_valid_word(word):
    # Regular expression pattern to match valid words
    pattern = r"^[a-zA-Z0-9\-']+$"
    return re.match(pattern, word) is not None

ench_d = enchant.Dict("en_US")

def checkspellerror(file_path):

    try:

        with open(file_path, 'r') as file:
            content = file.read()

        #cleaning of text 
        tokens = word_tokenize(content)
        word_frequency = {}
        cleaned_tokens=[]
        # Cleaning- optional 
        # cleaned_tokens = [token for token in tokens if token.isalpha()] # keeping only text with all aplhabetic words
        for token in tokens:
            if token not in word_frequency:
                word_frequency[token] = 1
            else:
                word_frequency[token] = +1 
            if token=="END-OF-CORPUS":
                break           
            if is_valid_word(token):
                cleaned_tokens.append(token)
          

            
        stopwords = nltk.corpus.stopwords.words('english')  
        
        filtered_tokens = [token for token in cleaned_tokens if token not in stopwords] # removing stopwords (optional )

        print(f"File Read successul and found {len(filtered_tokens)} Tokens/Words ")
        
        # Loading Enchant Dictionary 

        # ench_d = enchant.Dict("en_US")
        word_frequency = {}
        from tqdm import tqdm
        misspelled =[]
        for word in tqdm(filtered_tokens):
            if ench_d.check(word) == False:
                misspelled.append(word)
        misspelled_list=list(set(misspelled))
        
        print(f"Out of {len(filtered_tokens)} Words there are {len(misspelled)} mis-spelled words and {len(misspelled_list)} distinct mispelled words ")

        ## Finding Nearest Correct spelling 

        json_output=[]
        for word in tqdm(misspelled_list):
            corrected_word = ench_d.suggest(word)
            json_output.append({word:corrected_word})

        with open('enchant_suggestion.json', 'w') as file:
             json.dump(json_output, file, indent=4)
        
        with open('original_corpus.txt','w') as file1:
              file1.write(content)

        with open('word_frequency', 'w') as file2:
            json.dump(word_frequency, file2)


        print("All suggestions are loaded to 'enchant_suggestion.json' file for Manual review ")

            
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading file '{file_path}'.")


with open("/home/gops/projects/woodfrog.tech/spellchecker/filepath.txt", 'r') as file:
    file_path = file.read()

checkspellerror(file_path)