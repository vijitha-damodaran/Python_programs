"""
Write a Python program that takes a file name as its argument. 
This file contains names of people and their corresponding contact numbers.

- Prompt the user to enter a few characters to search for.
- Print all the names that contain this sequence of characters 
     in the ascending order of their names
"""
import sys

def get_fname():
    if len(sys.argv)<2:
        fname=input('Enter the file name:')
    else:
        fname=sys.argv[1]
    return fname

def save_in_dict(FH):
    contact_dict=dict()
    content=FH.read()
    lines=content.split('\n')
    for line in lines:
        parts=line.split(':')
        contact_dict[parts[0]]=parts[1]
    return contact_dict

def search_word(contact_dict,search):
    key_list=contact_dict.keys()
    res=[item for item in key_list if search in item]
    return res

#main pgm starts from here
if __name__=="__main__":
    file=get_fname()
    search=input('Enter search:')
    with open (file) as FH:
        contact_dict=save_in_dict(FH)
    key_inc=search_word(contact_dict,search)
    print({elem:contact_dict[elem] for elem in sorted(key_inc)})
