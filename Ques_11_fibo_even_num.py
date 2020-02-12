"""
This program prints the first 12 "even" Fibonacci numbers
"""

def fibo_oper(num1,num2):
    """
    This function calculates the fibonacci numbers
    """
    num1=num1+num2
    num2=num1+num2
    return num1,num2
    
def fibo_even(count_limit):
    """
    This function tests the numbers are even or not upto the count
    """
    frst=1
    sec=1
    count=0
    while(count<count_limit):
        frst,sec=fibo_oper(frst,sec)
        if frst%2==0:
            print(frst)
            count+=1
        if sec%2 ==0:
            print(sec)
            count+=1
            
#main starting from here
count_limit=12
fibo_even(count_limit)
