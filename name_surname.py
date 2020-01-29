"""
Get the user’s first name and last name. 
then print the user’s name in the following order and format
- Name Surname
"""
def get_frst_name():
    res=input('Name:')
    return res

def get_surname():
    res=input('Surname:')
    return res

import string
name=get_frst_name()
surname=get_surname()
print(str.upper(name),str.upper(surname))
print('-'*len(name),'-'*len(surname))
print(surname+','+name)
