""" Takes a filename as argument 
    Creates a new file with the name
    "shuffle" appended to the original filename.
    The lines in the input are shuffled 
    and written into the new file
"""

from fileops import *
import sys
import random

def shuffler(lines):
    """ Shuffle a list of strings Input : list of strings
    Return : a new list with original strings shuffled
    """
    random.shuffle(lines)
    return lines

# Main starts here
if __name__ == "__main__":
    file=sys.argv[1]
    lines = get_lines(file)
    shuffled_lines = shuffler(lines)
    print(shuffled_lines)
    new_name = file[:-4] + "shuffle.txt" 
    write_lines(new_name, shuffled_lines)
