"""
Create a text file “num.txt” that contains one number per line. 
These numbers can be 1, 2, 3 or 4 digit numbers.

- Write a program to read the numbers from this file
- Discard all numbers that are not 3 digit numbers.
- From all the 3 digit numbers in the file,
    find and print the prime numbers in descending order.
"""
import sys

def get_fname():
    if len(sys.argv)<2:
        fname=input('Enter the file name:')
    else:
        fname=sys.argv[1]
    return fname

def no_of_dgt(value):
    count=0
    while value>0:
        value=value//10
        count+=1
    return count

def prime_num(lst):
    """
    returns prime numbers in a list
    """
    prime=list()
    for num in lst:
        if num==2:
            prime.append(num)
        elif num>2:
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
    file=get_fname()
    lst=list()
    with open (file) as FH:
        num=FH.readline()
        while num!='':
            num=int(num.strip('\n'))
            if no_of_dgt(num)==3:
                lst.append(num)
            num=FH.readline()
    prime_lst=prime_num(lst)
    desc_order(prime_lst)
    
#main starts from here
if __name__=="__main__":
    main()
