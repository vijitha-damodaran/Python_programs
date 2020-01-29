"""
Ask the user to enter a number. 
Find the number of digits in that number
"""
def get_number():
    res=int(input('Enter the no.:'))
    return res

def no_of_dgt(num):
    count=0
    while num>0:
        num=num//10
        count+=1
    print('no.of dgts=',count)

#main program starts from here
number=get_number()
no_of_dgt(number)
