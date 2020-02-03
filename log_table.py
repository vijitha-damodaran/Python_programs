"""
log table of base 10 for numbers 1 to 10. 
Then create a log table to base 10 for all numbers from 1 to 100 
that are multiples of 10
"""
def log_table_upto_10():
    lst=[]
    for num in range(1,11):
        res=math.log(num,10)
        lst.append(res)
    return lst

def log_table_multiple_of_10():
    lst=[]
    for item in range(10,101,10):
        res=math.log(item,10)
        lst.append(res)
    return lst

def printing_value(lst_10,lst_mult):
    print('{0:15}  {1}'.format('\u0332'.join('Table1'),'\u0332'.join('Table2')))
    for item in range(0,10):
        print('{0:<2}-{1:<6}  {2:<3}-{3}'.format(item+1,round(lst_10[item],4),(item+1)*10, round(lst_mult[item],4)))

#main pgm starts from here
import math
import array
log_upto_10=[]
log_multiple_of_10=[]
log_upto_10=log_table_upto_10()
log_multiple_of_10=log_table_multiple_of_10()
printing_value(log_upto_10,log_multiple_of_10)
