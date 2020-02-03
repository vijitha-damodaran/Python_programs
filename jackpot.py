"""
This pgm checks if the number generated randomly is equal to
the digit sum of the number entered
"""
import sys
import sumops
import random
if len(sys.argv)>1:
    num=int(sys.argv[1])  
else:
    num=int(input('Enter a 5 digit no.:'))
dig_sum=sumops.dsum(num)
rand=random.randrange(1,51)
if rand==dig_sum:
    print('Hurray!!! U win the jackpot')
else:
    print('Better luck next time.')
    print('The random no. is=',rand)
