"""
Write a Python script that takes a file name as its first argument. 
Create a copy of the contents of this file satisfying the following conditions :
   
   - If the file name is “file.txt”,
       then the name of the new file should be “file-new.txt”
   - Every even line of the first file, should be
       repeated in the new file.
   - The first line of the first line, should be
       repeated after the last line of the first file.
   - A sample input and output file is shown below
"""
import sys

def get_file():
    if len(sys.argv)<2:
        fname=input('Enter file name:')
    else:
        fname=sys.argv[1]
    return fname

def main():
    fname=get_file()
    with open (fname) as FH:
        count=1
        lst=list()
        content=FH.readline()
        content=content.replace('\n','')
        frst=content
        while content!='':
            if count%2==0:
                lst.append(content)
                lst.append(content)
            else:
                lst.append(content)
            count+=1
            content=FH.readline()
            content=content.replace('\n','')
        lst.append(frst)
        print(lst)
        new_file=fname[:-4]+'-new'+fname[-4:]
    with open(new_file,'w') as FH:
        for items in lst:
            FH.write(items+'\n')
    with open (new_file) as FH:
        print(FH.read())

#main starts from here
if __name__=="__main__":
    main()
    
