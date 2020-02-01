"""
Write a Python function, that asks the user if he wants to continue. 
It should print “continue” and return True, if the user types in a yes,
irrespective of the case in which “yes” is typed. 

Import this function in any of your earlier exercises and 
run that exercise in a loop as long as the user enters “No”
"""
def cont_check():
    check=str.upper(input('Do you want to continue?:'))
    if check=='YES':
        print('continue')
        return True
    elif check=='NO':
        return False
