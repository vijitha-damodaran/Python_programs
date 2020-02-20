"""
Write a search and replace program in Python. 
This should prompt the user for which word to search,
  and what new word it should be replaced with. 
The file to be modified should be taken as argument to this program
"""
import sys

def get_file():
    if len(sys.argv)<2:
        fname=input('Enter the file name:')
    else:
        fname=sys.argv[1]
    return fname

def get_search():
    search=input('Enter word to be searched:')
    return search

def get_replace():
    replace=input('Enter the word to be replaced:')
    return replace

def main():
    file=get_file()
    search_word=get_search()
    replace_word=get_replace()
    new_content=list()
    with open (file) as FH:
        content=FH.readline()
        while content!='':
            content=content.split('\n')
            for line in content:
                words=line.split()
                for item in words:
                    if item==search_word:
                        words[words.index(item)]=replace_word
                new_content.append(" ".join(words))
            content=FH.readline()
        print(new_content)
    with open (file,'w') as FH:
        for item in new_content:
            FH.write(item+'\n')
    with open (file) as FH:
        print(FH.read())

#main starts from here
if __name__=="__main__":
    main()
