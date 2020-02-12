"""
Ask the user to enter a 3 digit number till he enters 0
Print the square root of only 3 digit positive numbers.
"""
def get_number():
    """
    this function is to get a positive input number
    """
    num=int(input('Enter the number:'))
    while num<0:
        print('Please enter a positive number')
        num=int(input('Enter the number again:'))
    return num

def num_of_dgt(number):
    """
    this function is to find the no. of digits
    """
    count=0
    while number>0:
        number=number//10
        count+=1
    return count

def print_sqrt_of_number(number):
    """
    this fn prints the sqrt of the num
    """
    print('square root is',number**0.5)

def sqrt_of_3digit_num():
    """
    this function is to check the input is 3 dgt or not and
    it gets the input till user enters 0
    """
    number=get_number()
    while number!=0:
        digit_num=num_of_dgt(number)
        if digit_num!=3:
            print('input a 3 digit number')
            number=get_number()
        else:
            print_sqrt_of_number(number)
            number=get_number()
    else:
        print('End')
        
#main starts from here
sqrt_of_3digit_num()
