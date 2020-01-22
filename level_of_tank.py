"""
This program gives signal to manage the level of a tank
if the tank is above or 80% full -> an alarm
if below or 20% full ->sms to buy more liquid
"""

def do_action(present, redmark, bluemark):
    if present>redmark:
        print('Close the valve')
    elif present<bluemark:
        print('Buy more liquid')
    else:
        print('Level is okay..Do nothing')
        
def get_current_level():
    current_value=int(input('Enter the current level of tank:'))
    return current_value

# Main starts from here
capacity = 900
high = capacity*80/100
low = capacity*20/100
level = get_current_level()
do_action(level, high, low)
