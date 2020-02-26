"""
You invited 10 friends to your house to play a game. 
Each one is asked to pick a card that contains a number between 99 and 999. 
The one with the maximum number wins the game. 
Simulate this game using Python
   - Which cards did each one pick ? 
   - Who won the game ?
"""

def get_guess():
    res=int(input('guess num:'))
    while (res<99 or res>999):
        res=int(input('guess num again:'))
    return res

def array_of_guess():
    lst=[]
    for item in range(0,10):
        print(item+1,'friend')
        guess=get_guess()
        if guess in lst:
            print('it is already selected')
            guess=get_guess()
        lst.append(guess)
    return lst

def max_value(lst):
    posi=lst.index(max(lst))
    return posi+1

#main pgm starts from here
if __name__ == "__main__":
#    import array
    guess_list=array_of_guess()
    friend_won=max_value(guess_list)
    print(friend_won,'th friend is the winner')
