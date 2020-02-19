"""
Write a Python script that takes a file name as its argument. 
In that file, find the line that has the maximum number of 
occurrences of the letter ‘e’
"""
import sys
import re
import string

def get_file_name():
    fname=sys.argv[1]
    return(fname)

def no_of_occurance(string_inp,sub_string):
    res=len(re.findall(sub_string,string_inp))
    return res

def check_for_max_occurance(fname,sub):
    with open(fname) as FH:
        content=FH.read()
        lines=content.split('\n')
        num_occur=list()
        for items in lines:
            num=no_of_occurance(items,sub)
            num_occur.append(num)
        max_value=max(num_occur)
        positions= [i for i, x in enumerate(num_occur) if x == max_value]
    return positions

#main starts from here
if __name__=="__main__":
    file=get_file_name()
    sub_string='e'
    positions=check_for_max_occurance(file,sub_string)
    print('max num of occurance of e at line',positions)
