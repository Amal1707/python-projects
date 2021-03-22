import json
from difflib import get_close_matches

data = json.load(open("English-Dictionary-cli\data.json"))

def getMeaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input(f"did you mean {get_close_matches(word, data.keys())[0]}?, enter Y if yes or N if no: ")
        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return "The word doesn't exist!, please check"
        else:
            return "didn't understand your entry"
    else:
        return "The word doesn't exist!, please check"



word = input("Enter a word: ")

output = getMeaning(word)
if type(output) == list:
    for line in output:
        print(line)
else:
    print(output)
