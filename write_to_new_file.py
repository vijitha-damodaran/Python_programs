"""
Write a Python script that takes a file name as its argument. 
Write the contents of this file to another file such that, 
each sentence is stored on a new line.
"""
import sys

def get_file_name():
    fname=sys.argv[1]
    return(fname)

def get_the_contents(fname):
    with open (fname) as FH:
        content=FH.read()
        content=content.replace('\n','')
        sentence=content.split('.')
        sentence=sentence[:-1]
        return sentence

def write_to_new(new_file,sentence):
    with open(new_file,'w') as new:
        for item in sentence:
            new.write(item+'.'+'\n')
    with open(new_file) as new:
        file=new.read()
        print(file)

#main starts from here
if __name__=="__main__":
    file=get_file_name()
    sentence=get_the_contents(file)
    write_to_new('new_file',sentence)
