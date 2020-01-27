"""
- Collect the runs scored for each ball faced by the batsman. 
    A dot ball is represented by a dot in input. 
    An empty line represents a wicket. 

- Finding the total runs scored ,strike rate,no. of balls wasted and
boundaries and sixes scored by the batsman
"""
def get_runs(lmt):
    """
    This function is for getting the runs scored by the batsman
    """
    count=1
    runs=[]
    run=0
    while count<=lmt and run!='':
        run =input('Enter run/ball:')
        runs.append(run)
        count+=1
    return runs,count-1

def get_no_of_balls():
    '''
    this function will get the tot balls in a test
    '''
    res=int(input('Enter the no.of ball:'))
    return res

def plot_of_batting(runs,ball):
    '''
    This function will print the plot of the batsman
    '''
    dot_ball=0
    six=0
    four=0
    run_tot=0
    for value in runs:
        if(value=='.'):
            dot_ball+=1
        if(value=='4'):
            four+=1
        if(value=='6'):
            six+=1
        if not (value=='.' or len(value)==0):
            run_tot=run_tot+int(value)
    strike_rate=run_tot/ball
    print('No.of balls wasted:',dot_ball)
    print('No.of boundaries:',four)
    print('No.of sixes:',six)
    print('Total runs scored:',run_tot)
    
def main():
    '''
    main function
    '''
    import array
    no_of_balls_per_test=get_no_of_balls()
    runs_scored,balls_faced=get_runs(no_of_balls_per_test)
    plot_of_batting(runs_scored,balls_faced)

#main starts from here
main()
