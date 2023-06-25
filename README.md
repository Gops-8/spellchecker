

			Python Spell Correction Program
Problem Statement  : 
The objective is to build a solution that allows the detection and the correction of spelling mistakes in the English language. Most common spelling mistakes occur for the following reasons: Deletion, Replacement, Transposition and Insertion.

Description : 
We have developed two python scripts 
checkspelling.py -  This script will read the text corpus taking the filepath(file location) as input and proprocess and generate a json file with suggestions of correct spelling for manual review .
replacetext.py - This script will take read the json file and read the misspelled word with the first suggestion and replace the word in text corpus 
Methodology used for Preprocessing : 
In the first step we are using word tokenizer of nltk libary to get all the words from the large text corpus and filter it with all the alphabetic words
Correction approach: 
After testing out multiple open sourced modules to find the nearest distance like textblob, pyspellchekcher , Bert Transformers,aspell-python and pyaspell.  we figured out the PyEnchant library works best on the the data set though it is time consuming but the accuracy is high compared to other libraries 

Reference : AbiWord/enchant: enchant spellchecking library (github.com)

Known Limitations : 
The Libary is not 100% accurate and it depends on Levenshtein Distance to suggest correct word . We will have to do manual review and replacement for some of the misspelled words 

We can improve by providing common nouns specific to the usecase and might not a dictionary word (eg Sagemaker) and tryout multiple configuration of enchant 

Currently i am using regular expression to replace the misspelled words with correct word but it is highly time consuming (93min) and this can be replaced with some other method 




Dependencies : 
Python 3(PyEnchant,nltk,re,json,tqdm) 

How To Use : 
Step1: Install Python3 
Step2: create a new environment (optional) and install depencencies 
“pip install -r requirement.txt “ on terminal 


Step3: Open checkspelling.py file and replace line #70 with path for the file and run the program (“python checkspelling.py” on terminal) 

Step4 : “enchant_suggestion.json” file will be generated after completing of above script open it review and replace the first suggestion with the accurate spelling 

Eg: #27 is the misspelled one and #28-#35 is the suggestion and #28 is the word it will replace if not manually adjusted 


Step5 : Run the “replacetext.py” script . it will read the json file as well as the text corpus and replace the mis-spelled word with the first suggestion and produce “corrected_corpus.txt” as output 
					


Some Stats for corpus shared with request : 

There were 1196734 Tokens 
Enchant able to identify 193561 Mispelled tokens and 17475 were unique 
It took around 16m to find the mispelled words and 93m to replace the token 











