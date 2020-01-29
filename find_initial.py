"""
Get the user’s first name and last name.  
        Find his best possible initials by eliminating the last character 
        Expected output :
        Best possible initials of "Dharmender Singh" is :
        Dharme S
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
while len(surname)>1:
    name=name[:-1]
    surname=surname[:-1]
print('Best possible initials of "Dharmender Singh" is :',name,surname)
    
