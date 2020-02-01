"""
You invite home 10 of your closest friends and play a simple game of luck.
Each of your friend picks up a card numbered from 300 to 325. 
The person with the highest number wins
Make sure that no 2 friends get the same numbered card
"""
def get_guess():
    res=int(input('guess num:'))
    while (res<300 or res>325):
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
    import array
    guess_list=array_of_guess()
    friend_won=max_value(guess_list)
    print(friend_won,'th friend is the winner')
