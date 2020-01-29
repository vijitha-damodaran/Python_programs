"""
Ask the user to enter a number.
- If the number is a single digit number, add 7 to it, 
     and print the number in its unit’s place
- If the number is a two digit number, raise the number to the power of 5, 
     and print the last 2 digits
- If the number is a three digit number, ask user to enter another number. 
     Add the 2 numbers and print the last 3 digits
"""

def get_number():
    """
    This function is for getting the number from user
    """
    res = int(input('Enter the number:'))
    return res

def no_of_dgt(num):
    count=0
    while num>0:
        num=num//10
        count+=1
    return count

def do_1digit_oper(number):
    '''
    perform operation for 1 digit numbers
    '''
    res=number+7
    print(res%10)

def do_2digit_oper(number):
    '''
    perform operation for 2 digit numbers
    '''
    res=5**number
    print(res%100)

def do_3digit_oper(number):
    '''
    perform operation for 3 digit numbers
    '''
    sec_inpt=int(input('Enter the second input:'))
    res=number+sec_inpt
    print(res%1000)

def perform_check(value):
    """
    This function includes code for performing the check
    """
    dgt_num=no_of_dgt(value)
    if dgt_num==1:
        do_1digit_oper(value)
    elif dgt_num==2:
        do_2digit_oper(value)
    elif dgt_num==3:
        do_3digit_oper(value)
    else:
        print('Input must be 1 or 2 or 3 digit positive value')

def main():
    """
    main function
    """
    num=get_number()
    perform_check(num)
    
#Main program starts from here
main()
