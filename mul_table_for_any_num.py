#Multiplication table of a number using for
count = int(input('Count upto which multiplication to be done: '))
number=int(input('NUmber whose mul_table is required: '))
#number=range(1,count+1)
for item in range(1,count+1):
    res=item*number
    print(item,'*',number,'=',res)
