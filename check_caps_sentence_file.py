"""
Get the name of the text file from the user. 
Check if all the sentences in that text file begin with a capital letter
"""
import sys
def get_file_name():
    fname=sys.argv[1]
    return(fname)

def check_capital_sent(fname):
    count=0
    with open (fname) as FH:
        content=FH.read()
        content=content.replace('\n','')
        sent=content.split('.')
        sent=sent[:-1]
        for item in sent:
            if not item[0].isupper():
                print('Not beginning with an uppercase letter')
                break
            else:
                count+=1
        if len(sent)==count:
            print('All beginning with an uppercase letter')

#main starts from here
if __name__=="__main__":
    file=get_file_name()
    check_capital_sent(file)
