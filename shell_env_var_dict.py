"""
Shell Environment variables are shown below.

- Use “keys()” and “items()” methods to print the
names of all the environment variables

- Which environment variables has the longest name ?

- Print the names of all the environment variables in a sorted order

- Print the names and values of environment variables in the following format :

- NAME         = value1
- MORE_NAME    = longer_value2
- ANOTHER_NAME = val
- HOME         = some_value_3
"""
import sys

def get_fname():
    if len(sys.argv)<2:
        fname=input('Enter the file name:')
    else:
        fname=sys.argv[1]
    return fname

def save_in_dict(FH):
    shell_dict=dict()
    content=FH.read()
    content=content.split('\n')
    for items in content:
        parts=items.split('=')
        shell_dict[parts[0]]=parts[1]
    return shell_dict

#main pgm starts from here
if __name__=="__main__":
    file=get_fname()
    with open (file) as FH:
        shell_dict=save_in_dict(FH)
    env_var_long=[name for name in sorted(shell_dict.keys(),key=len,reverse=True)]
    length=len(env_var_long[0])
    print('Env variable with longest name:',env_var_long[0])    
    print('Env variables in sorted order:',[name for name in sorted(shell_dict.keys())])
    for key in shell_dict.keys():
        print('{0:<20}={1:<10}'.format(key,shell_dict[key]))
