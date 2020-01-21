""" 
Prompting to enter name and Printing Hello username using function
"""

def get_username():
    """ 
    Prompts the user to enter his name
    """
    user_name =input('Enter your name:')
    return user_name

def say_hello(user):
    """
    Greet the user by saying Hello followed by his name
    """
    print("Hello",user,"!!!")

def main():
    '''
    Main function of the program
    '''
    name = get_username()
    say_hello(name)
    
# Main starts from below
main()
