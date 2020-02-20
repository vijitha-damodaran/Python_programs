"""
Ask the user to enter a 3 digit number, till he enters 0. 
Discard all numbers that are not 3 digit numbers. 
From all the 3 digit numbers entered by the user, 
     find and print the prime numbers in descending order
"""

def get_number():
    number=int(input('Enter the num:'))
    return number

def no_of_dgt(value):
    count=0
    while value>0:
        value=value//10
        count+=1
    return count

def prime_num(lst):
    """
    returns prime numbers in alist
    """
    prime=list()
    for num in lst:
        for val in range(2,num//2+1):
            if num%val==0:
                break
        else:
            prime.append(num)
    return prime
            
def desc_order(lst):
    lst.sort(reverse=True)
    print(lst)
    
def main():
    lst=list()
    numbr=get_number()
    dgt=no_of_dgt(numbr)
    if numbr==0:
        print('ERROR')
    else:
        while numbr!=0:
            if dgt==3:
                lst.append(numbr)
            numbr=get_number()
            dgt=no_of_dgt(numbr)
        prime_lst=prime_num(lst)
        desc_order(prime_lst)
#main starts from here
main()
