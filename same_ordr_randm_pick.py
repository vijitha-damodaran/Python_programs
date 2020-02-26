"""
Ask the user to enter any 10 numbers as input. 
Randomly pick any 5 numbers from this list 
  but print them in the same order as given by the user.
"""
import random

def get_num_lst():
    """
    getting the number list from user
    """
    lst=list()
    print('Enter numbers')
    count=0
    while count<10:
        print(str(count+1)+':',end='');num=int(input())
        lst.append(num)
        count+=1
    return lst

def get_key(x):
    return x[0]
    
def main():
    index_lst=list()
    num_lst=get_num_lst()
    rand_nums=random.sample(num_lst,5)
    print('random numbers are',rand_nums)
    for element in rand_nums:
        index=num_lst.index(element)
        data=(index,element)
        index_lst.append(data)
    index_lst.sort(key=get_key)
    
    #printing the result
    print('new sorted list in the same order as entered:',end=' ')
    for item in index_lst:
        print(item[1],end=',')
    
#main starts from here
main()
