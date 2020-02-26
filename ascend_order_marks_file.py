"""
Create a text file called “students.txt”. 
Each line should be of the form
“student_name : student_marks”

- Write a Python program to read the contents from this file.
- Print the names and marks of all students 
      who have scored more than 90% marks, 
      in ascending order of their marks.
"""

import sys

def get_fname():
    if len(sys.argv)<2:
        fname=input('Enter the file name:')
    else:
        fname=sys.argv[1]
    return fname

def get_key(x):
    max_tot=600
    return x[1]*100/max_tot

def read_file(file):
    with open (file) as FH:
        data_lst=list()
        line=FH.readline()
        while line!='':
            parts=line.split(':')
            data=(parts[0],int(parts[1]))
            data_lst.append(data)
            line=FH.readline()
    return data_lst

def main():
    file=get_fname()
    max_tot=600
    data_lst=read_file(file)
    data_lst.sort(key=get_key)
    for data in data_lst:
        if (data[1]*100/max_tot)>90:
            print(data[0],':',data[1])

#main starts from here
if __name__=="__main__":
    main()
