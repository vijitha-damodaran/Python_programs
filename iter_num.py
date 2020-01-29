"""
Ask the user to enter a number.
- If the user enters a number as 5, then
generate the following string :
- 00001111222233334444

- If the user enters the number as 3, then
generate the following string :
- 001122
"""

def get_number():
    res=int(input('Enter number:'))
    return res

def do_oper(num):
    count=0
    value=''
    while count<num:
        string=str(count)*(num-1)
        value=value+string
        count+=1
    print(value)
    
#main pgm starts from here
number=get_number()
do_oper(number)
