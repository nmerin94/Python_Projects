import json  # Library lists https://docs.python.org/3/library/index.html
from difflib import SequenceMatcher as seq
data =  json.load(open("data.json"))

def translate(w) :
    w = w.lower()
    if w in data:
        return(data[w])
    else :
        max_rat = 0
        for ob in data.keys():
            cur_rat = seq(None,ob,w).ratio()
            if (max_rat <= cur_rat):
                max_rat = cur_rat
                str = ob
        if(max_rat < .6):
            return 0
        else :
            prompt =  input("Did you mean %s ? (y/n) : " % (str))
            if(prompt == 'Y'  or prompt == 'y'):
                return(data[str])
            else:
                return 0

word = input("Enter the word : ")

str_list = translate(word)

if(str_list == 0):
    print("Sorry , the word does'nt exist ! ")
else:
    for i in str_list:
        print(i)
