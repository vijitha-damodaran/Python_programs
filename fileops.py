def get_lines(filename):
    """ Reads the contents of filename
        and returns the - File handle
        - List of all lines of the file
    """
    line=[]
    with open(filename,'r') as veg:
        line=veg.readlines()
        return line
    
def write_lines(filename, lines):
    """ Writes the lines into the a file whose
        filename is given as argument
    """
    with open(filename,'w+') as writer:
        writer.writelines(lines)
        
#Main starts from here
if __name__ == "__main__":
    lines=get_lines('vegetables.txt')
    write_lines('lines.txt','vegetables.txt')
