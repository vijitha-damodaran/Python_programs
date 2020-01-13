#Multiplication table of 17 using while
count = int(input('Count upto which multiplication to be done: '))
num=1
loop_inc=0
while loop_inc<count:
    res=num*17
    print(num,'*','17','=',res)
    loop_inc+=1
    num+=1
