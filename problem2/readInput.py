#This reads the input file and creates a square from the input by splitting between lines and
#spaces
import sys

def buildSquare():
    square = []
    curline = []
    #TODO take command line parameters for the file name here
    #filename = sys.argv

    #keeping the value hardcoded for now
    filename = 'Tests\input-board-filename.txt'
    with open(filename) as file:
        lines = file.read().splitlines()
        for line in lines:
            curline = line.split(' ')
            square.append(curline)
    return square