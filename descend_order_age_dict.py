"""
Write a Python program that prompts the user for a file. 
This file contains names of people and their ages. 

Read the file, and print the list with the oldest person’s name listed first. 
A sample file [ AGES.TXT ] is shown above :
"""
import sys

def get_fname():
    if len(sys.argv)<2:
        fname=input('Enter file name:')
    else:
        fname=sys.argv[1]
    return fname

def save_as_dict(FH):
    ages=dict()
    contents=FH.read()
    lines=contents.split('\n')
    for line in lines:
        parts=line.split('-')
        name=parts[0]
        age=parts[1]
        ages[name]=age
    return ages

def sorting(dict_age):
    for key in sorted(dict_age,key=dict_age.get,reverse=True):
        print(key,'-',dict_age[key])

#main program starts from here
if __name__=="__main__":
    file=get_fname()
    with open (file) as FH:
        age=save_as_dict(FH)
    sorting(age)   
