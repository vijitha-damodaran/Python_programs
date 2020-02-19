"""
From a file that contains a list of numbers.
Find the maximum number in that list. 
Also find the sum of all the numbers in that list.
"""
import sys

def get_file_name():
    fname=sys.argv[1]
    return fname

def max_of_list(FH):
    num_value=list()
    content=FH.read()
    content.replace('\n','')
    num=content.split(',')
    if num[len(num)-1]=='':
        num=num[:-1]
    for values in num:
        values=int(values)
        num_value.append(values)
    return max(num_value)

def sum_of_num(FH):
    sum_value=0
    content=FH.read()
    content.replace('\n','')
    num=content.split(',')
    if num[len(num)-1]=='':
        num=num[:-1]
    for values in num:
        sum_value=int(values)+sum_value
    return sum_value

#main starts from here
if __name__=="__main__":
    file=get_file_name()
    with open (file) as FH:
        print(max_of_list(FH))
    with open (file) as FH:
        print(sum_of_num(FH))
    
