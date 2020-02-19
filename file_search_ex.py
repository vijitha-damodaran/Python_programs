"""
Write a Python program that takes a file as the first argument 
   and a search word as the second argument. 
This script should print only those lines that have the search word
"""
import sys

def get_fname():
    if len(sys.argv)<2:
        fname=input("Enter the filename:")
    else:
        fname=sys.argv[1]
    return fname

def get_word():
    if len(sys.argv)<3:
        word=input("Enter the search word:")
    else:
        word=sys.argv[2]
    return word

def do_search(FH,word):
    word=word.lower()
    count=0
    line=list()
    content=FH.readline()
    while content!='':
        content=content.lower()
        parts=content.split()
        if word in parts:
            line.append(count+1)
        count+=1
        content=FH.readline()
    print('line numbers having',word,'in it are',line)
        
#main starts from here
if __name__=="__main__":
    file=get_fname()
    search_word=get_word()
    with open (file) as FH:
        do_search(FH,search_word)
