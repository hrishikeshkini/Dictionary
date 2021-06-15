import json
from difflib import get_close_matches
#importing the dataset
dataset = json.load(open('data.json'))

def search(word):
    if word in dataset:
        return dataset[word]
    elif word.upper() in dataset:
        return dataset[word.upper()]
    elif word.lower() in dataset:
        return dataset[word.lower()]
    elif word.title() in dataset:
        return dataset[word.title()]
    #This is get closest meaning to the word
    elif get_close_matches(word, dataset.keys()):
        print("You mean to say", get_close_matches(word, dataset.keys())[0], "instead of ", word)
        decide = input("Press y for Yes or n for No : ")
        if decide == "y":
            #To print the first closest meaning
            return dataset[get_close_matches(word, dataset.keys())[0]]
        elif decide == "n":
            return "Not found any meaning"
        else:
            return "Wrong Key"
    else:
        return "Not found any meaning"
            
        
    
word = input("Enter a word you want to search : ")
ans = search(word)
if type(ans) == list:
    for item in ans:
        print(item)
else:
    print(ans)
    
