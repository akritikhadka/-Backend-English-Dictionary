import json
import difflib
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(word):
    myword=word.lower()
    if myword in data:
        return data[myword]
    elif len(get_close_matches(myword,data.keys())) > 0 :
        return "Did you mean %s?" % get_close_matches(myword,data.keys())[0]
    else:
        return "Incorrect word.Please double check it"
word=input("\ninput enter the word\n")
print(translate(word))