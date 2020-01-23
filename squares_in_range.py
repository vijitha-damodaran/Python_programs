"""
Take a number as input from the user. 
Print all squares less than the input from 1. 
"""

def get_number():
    '''
    This function is to get the number
    '''
    num=int(input('Enter the number:'))
    return num

def square_range(lmt):
    """
    This function is find and print squares
    """
    sqrt_lmt=lmt**0.5
    if sqrt_lmt-int(sqrt_lmt)==0:
        sqrt_lmt=int(sqrt_lmt)-1
    else:
        sqrt_lmt=int(sqrt_lmt)
    for value in range(1,sqrt_lmt+1):
        print(value**2)
        
#Main program starts from here
limit=get_number()
square_range(limit)
