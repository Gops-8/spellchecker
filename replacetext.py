import json
from tqdm import tqdm
import re 

with open('original_corpus.txt', 'r') as file:
        content = file.read()

with open('enchant_suggestion.json', 'r') as file:
    json_data = file.read()
    data = json.loads(json_data)
    
new_content=content

file2 = open('nosuggestionfound.txt', 'w')
file2.write("Model not able to predict correct spelling for below mentioned words : \n")
for elem in tqdm(data):
    for key, value in elem.items():
        rplc_w=key
        try:
             crct_w=value[0]
             pattern = r'\b{}\b'.format(re.escape(rplc_w))
             new_content = re.sub(pattern, crct_w, new_content)
        except:
              file2.write(rplc_w+'\n')
          

with open('corrected_corpus.txt', 'w') as file2:
        file2.write(new_content)


