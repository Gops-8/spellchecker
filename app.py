from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch


def check_spelling_errors(file_path):
    # Load the pretrained language model and tokenizer
    model_name = "bert-base-cased"
    model = AutoModelForTokenClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    try:
        with open(file_path, 'r') as file:
            content = file.read()

            # Tokenize the text
            tokens = tokenizer.tokenize(content)
            inputs = tokenizer.encode(content, return_tensors="pt")

            # Perform spell checking
            with torch.no_grad():
                outputs = model(inputs)[0]
                predictions = torch.argmax(outputs, dim=2)[0]

            # Identify misspelled words and suggest corrections
            misspelled_words = []
            for token, prediction in zip(tokens, predictions):
                if prediction.item() == 1:  # 1 corresponds to "I-ORG" in BERT
                    misspelled_words.append(token)

            if len(misspelled_words) > 0:
                print("Misspelled words found:")
                for word in misspelled_words:
                    print(f"Word: {word}")
                    # Implement your own logic to suggest corrections for misspelled words
            else:
                print("No spelling errors found.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading file '{file_path}'.")

# Provide the path to the text file you want to check for spelling errors
file_path = 'path/to/your/text/file.txt'

# Call the function to perform spell checking
check_spelling_errors(file_path)
