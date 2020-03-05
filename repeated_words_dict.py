"""
Write a Python program that takes a file name as its argument. 
This program should count the occurrences of all the words in a file.

   - It should then print the top 10 most repeated words 
        in the descending order of their count.
   - Print a separate list of all the words that
        are not repeated in that file.
"""
import sys

def get_fname():
    if len(sys.argv)<2:
        fname=input('Enter file name:')
    else:
        fname=sys.argv[1]
    return fname

def save_in_dict(FH):
    word_count=dict()
    content=FH.read()
    words=content.replace('\n','').replace('.','').replace(',','').split(' ')
    for word in words:
        word=word.lower()
        if word in word_count.keys():
            word_count[word]=word_count[word]+1
        else:
            word_count[word]=0
    return word_count

#main program starts from here
if __name__=="__main__":
    file=get_fname()
    with open (file) as FH:
        word_dict=save_in_dict(FH)
    print('10 most repeated words are',{key: word_dict[key] for key in sorted(word_dict,key=word_dict.get,reverse=True)[:10]})
    print('words that are not repeated are',[key for key in word_dict.keys() if word_dict[key]==0])
