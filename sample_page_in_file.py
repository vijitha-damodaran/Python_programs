"""
Write a program that generates a HTML file. 
Prompt the user for webpage title and webpage body contents. 
The webpage body should contain 
    one main header, 
    one sub header, and 
    at least 2 paragraphs
"""
import string

def get_inp():
    webpage_title=input('Enter the webpage title:')
    main_header=input('Enter the main_header:')
    sub_header=input('Enter the sub_header:')
    para_1=input('first paragraph:')
    para_2=input('sec paragraph:')
    return webpage_title,main_header,sub_header,para_1,para_2

def main(webpage_title,main_header,sub_header,para_1,para_2):
    with open ('new_page.txt','w') as FH:
        FH.write('\n')#print()
        FH.write('\n')#print()
        FH.write('\n')#print()
        FH.write(('{:^40s}'.format((webpage_title)))+'\n')
        FH.write(('{:^40s}'.format((len(webpage_title)*'-')))+'\n')
        FH.write(('{:^20s}'.format(main_header))+'\n')
        FH.write(('{:^10s}'.format(sub_header))+'\n')
        FH.write('\n')#print()
        FH.write(('{:<s}'.format(para_1))+'\n')
        FH.write('\n')#print()
        FH.write(('{:<s}'.format(para_2))+'\n')
    with open ('new_page.txt') as FH:
        print(FH.read())
#main starts from here
if __name__=="__main__":
    webpage_title,main_header,sub_header,para_1,para_2=get_inp()
    main(webpage_title,main_header,sub_header,para_1,para_2)
