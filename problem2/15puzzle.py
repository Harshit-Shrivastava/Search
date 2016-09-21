#This is a classic 15-puzzle problem with one variation: When the empty tile is
#on the edge of the board, the tile on the opposite side of the board can be slided into the opening.
#The goal of the puzzle is to nd the shortest possible sequence of moves that restores the canonical configuration
# (on the left above) given an initial board configuration.
#The goal is to find a solution to this problem eciently using A* search
#Input configuration is in the file input.txt

import sys
from readInput import buildSquare
from solve import aStar

if __name__ == "__main__":
    square = buildSquare()
    print(square)
    print(aStar(square))
