"""
Write a Python program that takes a file name as its argument. 
This file contains names of people and their corresponding contact numbers. 

Read the file, and print the list in the ascending order of their names. 
A sample file [ CONTACT_LIST.TXT ] is shown below :
"""
import sys

def get_fname():
    if len(sys.argv)<2:
        fname=input('Enter file name:')
    else:
        fname=sys.argv[1]
    return fname

def save_as_dict(FH):
    contact=dict()
    contents=FH.read()
    lines=contents.split('\n')
    for line in lines:
        parts=line.split(':')
        name=parts[0]
        num=parts[1]
        contact[name]=num
    return contact

def sorting(contact):
    for key in sorted(contact):
        print(key,':',contact[key])

#main program starts from here
file=get_fname()
with open (file) as FH:
    contact=save_as_dict(FH)
sorting(contact)   
