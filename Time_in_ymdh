#if you can do a thing in 10000hours,
#how many years months days and hrs needed 
#to complete a task working n hours per day

def divide(a,b):
    q=a//b
    r=a%b
    return q,r
    
Time=10000
hrs_per_day= int(input('ENTER THE HOURS/DAY: '))
day,hrs = divide(Time,hrs_per_day)
mnth,day = divide(day,30)
year,mnth = divide(mnth,12)
print(year,'years', mnth,'months', day,'days', hrs,'hours')
