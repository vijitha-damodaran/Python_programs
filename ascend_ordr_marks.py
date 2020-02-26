"""
Ask user to enter the student’s name followed by his total marks in the
SSLC exam. An empty line indicates the end of input. Print the names and
marks of all students who have scored more than 90% marks,
in ascending order of their marks
"""
def get_data():
    name=input('Enter student name:')
    if name=='':
        return name,False
    else:
        mark=int(input('Enter mark:'))
    return name,mark

def get_key(x):
    max_tot=600
    return x[1]*100/max_tot

def main():
    data_lst=list()
    max_tot=600
    data=get_data()
    while data[0]!='':
        data_lst.append(data)
        data=get_data()
    data_lst.sort(key=get_key)
    for data in data_lst:
        if (data[1]*100/max_tot)>90:
            print(data[0],':',data[1])
            
#main starts from here
if __name__=="__main__":
    main()
