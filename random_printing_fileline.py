"""
Read the contents of a file and randomly print any one line from that file.
"""
from fileops import *
import sys
import random

def select_random_line(filename):
    lines=get_lines(file)
    print("random line is: ",random.choice(lines))

# Main starts here
if __name__ == "__main__":
    file=sys.argv[1]
    select_random_line(file)
