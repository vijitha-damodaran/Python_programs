"""
Write a function that accepts 2 lists as arguments. 
Both these 2 lists must be already sorted in the ascending order
This function should combine the lists into a sorted order and return the
resulting list. This function should not use any built-in sort function
or method. 
    pass the following 2 lists as arguments to your function 
    and print the sorted result.

    - left  = [4, 17, 21, 47, 69, 75, 91, 97]
   - right = [3, 10, 11, 14, 18, 21, 44, 55, 76,97]
"""

def get_combine_sort_lst(frst,sec):
    tot=frst+sec
    length=len(tot)
    res=list()
    for i in range(length):
        for j in range(length):
            if tot[i]<tot[j]:
                tot[i],tot[j]=tot[j],tot[i]
    [res.append(x) for x in tot if x not in res]
    print(tot)
    print('sorted result:',res)
    
#main starts from here
if __name__=="__main__":
    frst_lst=[4, 17, 21, 47, 69, 75, 91, 97]
    sec_lst=[3, 10, 11, 14, 18, 21, 44, 55, 76,97]
    get_combine_sort_lst(frst_lst,sec_lst)
