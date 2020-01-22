"""
This program helps to check if the given number is 2 digit or 3 digit
"""

def get_number():
    """
    This function is for getting the number from user
    """
    res = int(input('Enter the number:'))
    return res

def perform_check(value):
    """
    This function includes code for performing the check
    """
    if 99<value<1000 or -1000<value<-99:
        print(value,"is a three digit number")
    elif 9<value<100 or -100<value<-9:
        print(value,"is a two digit number")
    else:
        print(value)

def main():
    """
    main function
    """
    num1=get_number()
    num2=get_number()
    perform_check(num1)
    perform_check(num2)
    
#Main program starts from here
main()
