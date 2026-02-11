import json;
import random;

def randomize_questions():
    with open("questions.json", "r") as file:
        data = json.load(file);                 #allows the contents of questions.json to be called as a variable
        random.shuffle(data);                   #shuffles the data groups

    print(json.dumps(data, indent=4));          #prints the data of questions.json

randomize_questions();                          #calls the entire randomize_questions() function

#IMPORTANT, to be merged with the countdown function eventually in the comlplete logic file


#IGNORE, used to test randomization functionality
#>==================================================

'''
def print_test(): 
    with open("jsonTest.json", "r") as file:
        data = json.load(file);
        random.shuffle(data);    
    
    print(json.dumps(data, indent=4));

print_test();
'''

#>==================================================