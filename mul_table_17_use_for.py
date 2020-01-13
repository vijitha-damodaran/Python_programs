#Multiplication table of 17 using for
count = int(input('Count upto which multiplication to be done: '))
number=range(1,count+1)
for item in number:
    res=item*17
    print(item,'*','17','=',res)
