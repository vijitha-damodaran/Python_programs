"""
Write a search and replace program in Python. 
This should first take the original text as input by prompting the user for it. 
It should then, prompt the user for which word to search, 
and what new word it should be replaced with.
"""
import sys

def get_text():
    if len(sys.argv)==1:
        text=input('Enter the text:')
    else:
        text=sys.argv[1]
    return text

def get_search_word():
    word=input('Word to be searched:')
    return word

def get_replace_word():
    replace=input('Replace:')
    return replace

def do_search_replace(text,search,replace):
    if (text.find(search))!=-1:
        text=text.replace(search,replace)
        print('New text is:')
        print(text)
    else:
        print('word not found in the text')

#main program starts from here
if __name__=="__main__":
    text=get_text()
    search_word=get_search_word()
    new_word=get_replace_word()
    do_search_replace(text,search_word,new_word)
