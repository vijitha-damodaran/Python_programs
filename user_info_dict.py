"""
Read passwd file and list all users mentioned in that file in ascending order
of their user id. Also mention the user’s real name and home directory
in the output. 
"""
import sys

def get_fname():
    if len(sys.argv)<2:
        fname=input('Enter file name:')
    else:
        fname=sys.argv[1]
    return fname

#main pgm starts from here
if __name__=="__main__":
    file=get_fname()
    pw_dict=dict()
    with open (file) as FH:
        line=FH.readline()
        while line!='':
            parts=line.replace('\n','').split(':')
            pw_dict[parts[0]]=parts[3:]
            line=FH.readline()
    print('o/p:',{key:pw_dict[key][:-1] for key in sorted(pw_dict,key=lambda x:pw_dict[x][0])})
