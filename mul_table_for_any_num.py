"""
Prints Multiplication table of a number upto the count
"""

def get_number():
    '''
    This function is for getting the number from the user
    '''
    num=int(input('NUmber whose mul_table is required: '))
    return num

def print_mtable(num):
    '''
    This function prints the multiplication table
    '''
    count = int(input('Count upto which multiplication to be done: '))
    for item in range(1,count+1):
        res=item*num
        print(item,'*',num,'=',res)

def main():
    '''
    Main function
    '''
    number=get_number()
    print_mtable(number)

#Main program starts from here
main()
