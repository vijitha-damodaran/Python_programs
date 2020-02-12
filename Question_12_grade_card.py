"""
The pass marks for each subject is as follows :
          -- Pass marks for English : 25/75
          -- Pass marks for Science Theory : 25/75
          -- Pass marks for Science Practical : 8/25
          -- Pass marks for Science : 35/100
          -- Pass marks for Mathematics : 35/100
Based on the marks scored by the student, grade them according to the following criteria :
          -- Grade A : if Total > 90%
          -- Grade B : if Total > 75%
          -- Fail is any score is less than pass marks
          -- Average otherwise
"""

def get_marks():
    """
    this function is to get the input marks
    """
    eng=int(input('Marks scored in English: '))
    sci_theo=int(input('Marks scored in Science theory: '))
    sci_pract=int(input('Marks scored in Science practical: '))
    maths=int(input('Marks scored in Maths: '))
    return eng,sci_theo,sci_pract,maths

def get_grades(eng,sci_theo,sci_pract,maths,tot_max):
    """
    this function calculates the grade
    """
    sci_tot =sci_theo+sci_pract
    total=eng+sci_tot+maths
    tot_perc =total*100/tot_max
    if eng<25 or sci_theo<25 or sci_pract<8 or sci_tot<35 or maths<35:
        print('Fail')
    elif tot_perc>90:
        print('Grade A')
    elif tot_perc>75 and tot_perc<=90:
        print('Grade B')
    else:
        print('Average')
        
#main starts from here
if __name__=="__main__":
    eng,sci_theo,sci_pract,maths=get_marks()
    tot_max=275
    get_grades(eng,sci_theo,sci_pract,maths,tot_max)
