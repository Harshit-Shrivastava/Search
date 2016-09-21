from library import createElement
from library import fringePriority
import sys
import copy

goalState = [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','0']]

def successor(curStateObject):
    priority, elem = curStateObject
    curState = elem.state
    curCostSoFar = elem.costSoFar
    curHeuristic = elem.heuristic
    index = indexSearch(curState, '0')
    r = index[0]
    c = index[1]

    heuristic1 = sys.maxint
    heuristic2 = sys.maxint
    heuristic3 = sys.maxint
    heuristic4 = sys.maxint
    tempState1 = [[]]
    tempState2 = [[]]
    tempState3 = [[]]
    tempState4 = [[]]

    #TODO: Write the edge conditions where the empty tile can move only in 2 or 3 positions
    if(r == 0 and c == 0):
        # moving left
        tempState1 = copy.deepcopy(curState)
        tempState1[0][0], tempState1[0][3] = tempState1[0][3], tempState1[0][0]
        heuristic1 = heuristicCalculator(tempState1, goalState)

        # moving up
        tempState2 = copy.deepcopy(curState)
        tempState2[0][0], tempState2[3][0] = tempState2[3][0], tempState2[0][0]
        heuristic2 = heuristicCalculator(tempState2, goalState)

        # moving down
        tempState3 = copy.deepcopy(curState)
        tempState3[r][c], tempState3[r+1][c] = tempState3[r+1][c], tempState3[r][c]
        heuristic3 = heuristicCalculator(tempState3, goalState)

        # moving right
        tempState4 = copy.deepcopy(curState)
        tempState4[r][c], tempState4[r][c+1] = tempState4[r][c+1], tempState4[r][c]
        heuristic4 = heuristicCalculator(tempState4, goalState)

    elif(r == 3 and c == 0):
        # moving left
        tempState1 = copy.deepcopy(curState)
        tempState1[3][0], tempState1[3][3] = tempState1[3][3], tempState1[3][0]
        heuristic1 = heuristicCalculator(tempState1, goalState)

        # moving up
        tempState2 = copy.deepcopy(curState)
        tempState2[r][c], tempState2[r-1][c] = tempState2[r-1][c], tempState2[r][c]
        heuristic2 = heuristicCalculator(tempState2, goalState)

        # moving down
        tempState3 = copy.deepcopy(curState)
        tempState3[3][0], tempState3[0][0] = tempState3[0][3], tempState3[3][0]
        heuristic3 = heuristicCalculator(tempState3, goalState)

        # moving right
        tempState4 = copy.deepcopy(curState)
        tempState4[r][c], tempState4[r][c+1] = tempState4[r][c+1], tempState4[r][c]
        heuristic4 = heuristicCalculator(tempState4, goalState)

    elif(r == 0 and c == 3):
        # moving left
        tempState1 = copy.deepcopy(curState)
        tempState1[r][c], tempState1[r][c-1] = tempState1[r][c-1], tempState1[r][c]
        heuristic1 = heuristicCalculator(tempState1, goalState)

        # moving up
        tempState2 = copy.deepcopy(curState)
        tempState2[0][3], tempState2[3][3] = tempState2[3][3], tempState2[0][3]
        heuristic2 = heuristicCalculator(tempState2, goalState)

        # moving down
        tempState3 = copy.deepcopy(curState)
        tempState3[r][c], tempState3[r+1][c] = tempState3[r+1][c], tempState3[r][c]
        heuristic3 = heuristicCalculator(tempState3, goalState)

        # moving right
        tempState4 = copy.deepcopy(curState)
        tempState4[0][3], tempState4[0][0] = tempState4[0][0], tempState4[0][3]
        heuristic4 = heuristicCalculator(tempState4, goalState)

    elif(r == 3 and c == 3):
        # moving left
        tempState1 = copy.deepcopy(curState)
        tempState1[r][c], tempState1[r][c-1] = tempState1[r][c-1], tempState1[r][c]
        heuristic1 = heuristicCalculator(tempState1, goalState)

        # moving up
        tempState2 = copy.deepcopy(curState)
        tempState2[r][c], tempState2[r-1][c] = tempState2[r-1][c], tempState2[r][c]
        heuristic2 = heuristicCalculator(tempState2, goalState)

        # moving down
        tempState3 = copy.deepcopy(curState)
        tempState3[3][3], tempState3[0][3] = tempState3[0][3], tempState3[3][3]
        heuristic3 = heuristicCalculator(tempState3, goalState)

        # moving right
        tempState4 = copy.deepcopy(curState)
        tempState4[3][3], tempState4[3][0] = tempState4[3][0], tempState4[3][3]
        heuristic4 = heuristicCalculator(tempState4, goalState)

    elif(r == 0):
        # moving left
        tempState1 = copy.deepcopy(curState)
        tempState1[r][c], tempState1[r][c-1] = tempState1[r][c-1], tempState1[r][c]
        heuristic1 = heuristicCalculator(tempState1, goalState)

        # moving up
        #tempState2 = curState
        #tempState2[x][y], tempState2[x][y - 1] = tempState2[x][y - 1], tempState2[x][y]
        #heuristic2 = heuristicCalculator(tempState2, goalState)

        # moving down
        tempState3 = copy.deepcopy(curState)
        tempState3[r][c], tempState3[r+1][c] = tempState3[r+1][c], tempState3[r][c]
        heuristic3 = heuristicCalculator(tempState3, goalState)

        # moving right
        tempState4 = copy.deepcopy(curState)
        tempState4[r][c], tempState4[r][c+1] = tempState4[r][c+1], tempState4[r][c]
        heuristic4 = heuristicCalculator(tempState4, goalState)

    elif(r == 3):
        # moving left
        tempState1 = copy.deepcopy(curState)
        tempState1[r][c], tempState1[r][c-1] = tempState1[r][c-1], tempState1[r][c]
        heuristic1 = heuristicCalculator(tempState1, goalState)

        # moving up
        tempState2 = copy.deepcopy(curState)
        tempState2[r][c], tempState2[r-1][c] = tempState2[r-1][c], tempState2[r][c]
        heuristic2 = heuristicCalculator(tempState2, goalState)

        # moving down
        #tempState3 = curState
        #tempState3[x][y], tempState3[x][y + 1] = tempState3[x][y + 1], tempState3[x][y]
        #heuristic3 = heuristicCalculator(tempState3, goalState)

        # moving right
        tempState4 = copy.deepcopy(curState)
        tempState4[r][c], tempState4[r][c+1] = tempState4[r][c+1], tempState4[r][c]
        heuristic4 = heuristicCalculator(tempState4, goalState)

    elif(c == 0):
        # moving left
        #tempState1 = curState
        #tempState1[x][y], tempState1[x - 1][y] = tempState1[x - 1][y], tempState1[x][y]
        #heuristic1 = heuristicCalculator(tempState1, goalState)

        # moving up
        tempState2 = copy.deepcopy(curState)
        tempState2[r][c], tempState2[r-1][c] = tempState2[r-1][c], tempState2[r][c]
        heuristic2 = heuristicCalculator(tempState2, goalState)

        # moving down
        tempState3 = copy.deepcopy(curState)
        tempState3[r][c], tempState3[r+1][c] = tempState3[r+1][c], tempState3[r][c]
        heuristic3 = heuristicCalculator(tempState3, goalState)

        # moving right
        tempState4 = copy.deepcopy(curState)
        tempState4[r][c], tempState4[r][c+1] = tempState4[r][c+1], tempState4[r][c]
        heuristic4 = heuristicCalculator(tempState4, goalState)

    elif(c == 3):
        # moving left
        tempState1 = copy.deepcopy(curState)
        tempState1[r][c], tempState1[r][c-1] = tempState1[r][c-1], tempState1[r][c]
        heuristic1 = heuristicCalculator(tempState1, goalState)

        # moving up
        tempState2 = copy.deepcopy(curState)
        tempState2[r][c], tempState2[r-1][c] = tempState2[r-1][c], tempState2[r][c]
        heuristic2 = heuristicCalculator(tempState2, goalState)

        # moving down
        tempState3 = copy.deepcopy(curState)
        tempState3[r][c], tempState3[r+1][c] = tempState3[r+1][c], tempState3[r][c]
        heuristic3 = heuristicCalculator(tempState3, goalState)

        # moving right
        #tempState4 = curState
        #tempState4[x][y], tempState4[x + 1][y] = tempState4[x + 1][y], tempState4[x][y]
        #heuristic4 = heuristicCalculator(tempState4, goalState)

    else:
        #thinking the regular cases first
        #moving left
        tempState1 = copy.deepcopy(curState)
        tempState1[r][c], tempState1[r][c-1] = tempState1[r][c-1], tempState1[r][c]
        heuristic1 = heuristicCalculator(tempState1, goalState)

        #moving up
        tempState2 = copy.deepcopy(curState)
        tempState2[r][c], tempState2[r-1][c] = tempState2[r-1][c], tempState2[r][c]
        heuristic2 = heuristicCalculator(tempState2, goalState)

        #moving down
        tempState3 = copy.deepcopy(curState)
        tempState3[r][c], tempState3[r+1][c] = tempState3[r+1][c], tempState3[r][c]
        heuristic3 = heuristicCalculator(tempState3, goalState)

        #moving right
        tempState4 = copy.deepcopy(curState)
        tempState4[r][c], tempState4[r][c+1] = tempState4[r][c+1], tempState4[r][c]
        heuristic4 = heuristicCalculator(tempState4, goalState)

    bestMove = min (heuristic1, heuristic2, heuristic3, heuristic4)
    move = ''
    if(bestMove == heuristic1):
        curState = tempState1
        move = 'L'
    elif(bestMove == heuristic2):
        curState = tempState2
        move = 'U'
    elif(bestMove == heuristic3):
        curState = tempState3
        move = 'D'
    else:
        curState = tempState4
        move = 'R'
    elem.state = curState
    return elem

def aStar(curSquare):

    heuristic = heuristicCalculator(curSquare, goalState)
    #print heuristic

    #if initial and goal states are the same, return the initial state
    #this means that the square is already solved
    if (curSquare == goalState):
        return curSquare

    #if not, implement fringe as a priority queue and run A* search on it

    #creating a priority queue in python
    #example studied from http://www.bogotobogo.com/python/python_PriorityQueue_heapq_Data_Structure.php
    try:
        import Queue as Q
    except ImportError:
        import queue as Q
    fringe = Q.PriorityQueue()
    #example from the blog ends here

    #create an object to store the state, cost, heuristic, etc.
    tempFringeElem = createElement(curSquare,0,heuristic)
    tempFringePri = fringePriority(tempFringeElem)
    fringe.put((tempFringePri, tempFringeElem))
    #priority, elem = fringe.get()
    #print (elem).heuristic

    #creating a hash table as a dictionary to implement CLOSED


    #TODO: Need to think here, still not clear on the approach
    while not fringe.empty():
            s = successor(fringe.get())
            elem = s
            #elem, priority = s
            if elem == goalState:
                return
            cost = s.costSoFar + 1
            heuristic = heuristicCalculator(s.state, goalState)
            s.costSoFar = cost
            s.heuristic = heuristic
            tempFringePri = fringePriority(tempFringeElem)
            #print " %s" %move
            fringe.put(tempFringePri, s)
            return False

#function to find position of an element in an 2D list
#code from http://stackoverflow.com/questions/6518291/using-index-on-multidimensional-lists
def indexSearch(curState, elem):
    for row, i in enumerate(curState):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1
#code from stackoverflow.com ends here

#this function calculates the heuristic for the a-star algorithm
#heuristic is taken as the manhattan distance between the current position of the
def heuristicCalculator(square, goalState):
    heuristic = 0
    for i in range (0,4):
        for j in range (0,4):
            temp = square[i][j]
            index = indexSearch(goalState, temp)
            cur_manhattan_distance = abs(index[0] - i) + abs(index[1] - j)
            #print "%s %d %d" %(square[i][j],cur_manhattan_distance,heuristic)
            heuristic = heuristic + cur_manhattan_distance
    return heuristic