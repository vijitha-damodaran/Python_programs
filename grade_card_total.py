"""
This program calculates the grade of a student
given the marks scored in 3 subjects
"""

def get_marks():
    '''
    This function is for getting the marks
    '''
    eng=int(input('Marks scored in English: '))
    sci=int(input('Marks scored in Science: '))
    math=int(input('Marks scored in Maths: '))
    return eng,sci,math

def calc_grade(eng,sci,math,total_max):
    '''
    This function calculates the grade of the student
    '''
    total_scored=eng+sci+math
    total_perc =total_scored*100/total_max
    if total_perc>=90:
        print('First Class')
    if total_perc>=75 and total_perc<90:
        print('Second Class')
    if total_perc>35 and total_perc<75:
        print('Average')
    if total_perc<=35:
        print('Fail')

#Main program starts from here
total_maximum = 80+90+100
english,science,maths=get_marks()
calc_grade(english,science,maths,total_maximum)
