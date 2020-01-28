"""
Collect the names of the 2 batmen currently playing.
Who among them is currently at the non striker’s end ?
- Collect runs scored for each ball. 
    Make sure, you accumulate runs for the correct player based on who is facing the ball.
- Remember that players change positions at the end of each over. 
- The match ends after 30 balls, or if any batsman scores more than 60 runs.
- Print all the statistics for each batsman 
"""

def get_name_current_players():
    """
    This function is to get the name of players
    """
    frst=input('Enter current player1:')
    sec=input('Enter (non strikers end) player2:')
    return frst,sec

def get_runs(lmt):
    """
    This function is for getting the runs scored by the batsmen
    """
    sec_score=0
    count=1
    runs_frst=[]
    runs_sec=[]
    run=0
    run =input('Enter run/ball:')
    if run=='.':
        run='0'
    runs_frst.append(run)
    frst_score=int(run)
    while (count<lmt and run!='')and (frst_score<=60 and sec_score<=60):
        dup=int(run)
        if ((int(run)%2)!=0 or count%6==0):
            swap=runs_frst
            runs_frst=runs_sec
            runs_sec=swap
        if (int(run)%2)!=0 and count%6==0:
            swap=runs_frst
            runs_frst=runs_sec
            runs_sec=swap
        run =input('Enter run/ball:')
        if run=='.':
            run='0'
        runs_frst.append(run)
        if run=='':
            break
        elif(dup%2!=0 or count%6==0):
            sec_score+=int(run)
        else:
            frst_score+=int(run)
        count+=1
    if (int(runs_frst[-2]))%2!=0:
        swap=runs_frst
        runs_frst=runs_sec
        runs_sec=swap
    return runs_frst,runs_sec,len(runs_frst),len(runs_sec)

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
        if(value=='0'):
            dot_ball+=1
        if(value=='4'):
            four+=1
        if(value=='6'):
            six+=1
        if(value!=''):
            run_tot=run_tot+int(value)
    if ball==0:
        print('no balls faced')
    else:
        strike_rate=run_tot/ball
    print('No.of balls wasted:',dot_ball)
    print('No.of boundaries:',four)
    print('No.of sixes:',six)
    print('Total runs scored:',run_tot)
    print('Strike rate:',strike_rate)
    
def main():
    '''
    main function
    '''
    import array
    no_of_balls_per_test=get_no_of_balls()
    first,second=get_name_current_players()
    runs_frst_scored,runs_sec_scored,balls_faced_frst,balls_faced_sec=get_runs(no_of_balls_per_test)
    print(first)
    plot_of_batting(runs_frst_scored,balls_faced_frst)
    print(second)
    plot_of_batting(runs_sec_scored,balls_faced_sec)

#main starts from here
main()
