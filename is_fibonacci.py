"""
Check if a given number is a fibonacci number. 
If not, then print the closest fibonacci number to the given number
"""
def get_number():
    """
    This function is for getting the number from user
    """
    res = int(input('Enter the number:'))
    return res

def is_perfect_square(value):
    '''
    This function is to check the number is a perfect square or not
    '''
    if int(value**0.5)-(value**0.5)==0:
        return True
    else:
        return False

def close_fibo(value):
    '''
    This function is to find the closest fibo number
    '''
    frst=1
    sec=1
    while(value<frst or sec):
        frst=frst+sec
        if frst>value:
            break
        sec=frst+sec
        if sec>value:
            break
    if abs(frst-value)>abs(sec-value):
        print('Closest fibonacci number is',sec)
    elif abs(frst-value)<abs(sec-value):
        print('Closest fibonacci number is',frst)
    else:
        print('Closest fibonacci numbers are',frst,'and',sec)

def perform_check_fibo(num):
    '''
    This function check if the number is fibonacci or not
    '''
    if is_perfect_square(5*(num**2)+4) or is_perfect_square(5*(num**2)-4):
        print(num,'is a fibonacci number')
    else:
        close_fibo(num)

#main program startss from here
number=get_number()
perform_check_fibo(number)
