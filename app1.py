import json
import difflib
from difflib import get_close_matches
data=json.load(open("data.json"))
def translate(word):
    myword=word.lower()
    if myword in data:
        return data[myword]
    elif len(get_close_matches(myword,data.keys())) > 0 :
        yn=input("Did you mean %s ? Enter Y if yes and N if no :" % get_close_matches(myword,data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(myword,data.keys())[0]]
        elif yn=="N":
            return "word doesnot exist"
        else:
            return "We didnot understood what you want to say"
    else:
        return "Incorrect word.Please double check it"
word=input("\ninput enter the word\n")
output=(translate(word))
if type(output)== list :
    for item in output:
        print (item)
else:
    print (output)