"""
This program takes multiple sentences as input from the user. 
The last input is indicated by an empty line.
- Find the number of words entered
- Find the number of words that contain the vowel ‘a’
"""

def get_sentence():
    """
    This function is for getting the string from user
    """
    res = input('Enter the sentence:')
    return res

def num_words(lst):
    '''
    This function is to find the no. of words entered
    '''
    res=0
    for item in lst:
        res=res+len(item.split())
    print('No. of words entered=',res)

def containing_a(lst):
    '''
    This func is to count the no.of words containing a
    '''
    count=0
    for item in lst:
        for word in item.split():
            if word.find('a')==-1:
                continue
            else:
                count+=1
    print('No.of words containing a=',count)
    
def main():
    '''
    This is the main function
    '''
    import string
    import array
    list=[]
    word=get_sentence()
    while len(word)!=0:
        list.append(word)
        word=get_sentence()
    num_words(list)
    containing_a(list)

#main program starts from here
main()
