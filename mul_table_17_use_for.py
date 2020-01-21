""" 
This program prints
multiplication table of 17
"""

def print_mtable17():
    """ 
    Prints the multiplication table for 17
    upto the count given by the user
    """
    count = int(input('Count upto which multiplication to be done: '))
    number=range(1,count+1)
    for item in number:
        res=item*17
        print(item,'*','17','=',res)

# Main starts from here
print_mtable17()
