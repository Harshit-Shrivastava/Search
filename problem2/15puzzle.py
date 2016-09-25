# This is a classic 15-puzzle problem with one variation: When the empty tile is
# on the edge of the board, the tile on the opposite side of the board can be slided into the opening.
# The goal of the puzzle is to nd the shortest possible sequence of moves that restores the canonical configuration
# (on the left above) given an initial board configuration.
# The goal is to find a solution to this problem eciently using A* search
# Input configuration is in the file input.txt

from readInput import build_square
from solve import a_star,do
import time

if __name__ == "__main__":
    s = time.time()
    print(" ".join(a_star(build_square('Tests\input-board-filename.txt'))))
    #do(build_square('Tests\input-board-filename.txt'),a_star(build_square('Tests\input-board-filename.txt')))
    print (time.time()-s)
    """2 4 10 9
3 15 12 7
0 14 8 13
5 1 6 11"""
