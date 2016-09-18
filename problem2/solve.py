from library import createElement
from library import fringePriority

def successor(curStateObject):
    priority, elem = curStateObject
    curState = elem.state
    curCostSoFar = elem.costSoFar
    curHeuristic = elem.heuristic
    index = indexSearch(curState, '0')
    print index


def aStar(curSquare):
    goalState = [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','0']]
    heuristic = heuristicCalculator(curSquare, goalState)
    #print heuristic
    #creating a priority queue in python
    #example studied from http://www.bogotobogo.com/python/python_PriorityQueue_heapq_Data_Structure.php
    try:
        import Queue as Q
    except ImportError:
        import queue as Q
    fringe = Q.PriorityQueue()
    tempFringeElem = createElement(curSquare,0,heuristic)
    tempFringePri = fringePriority(tempFringeElem)
    fringe.put((tempFringePri, tempFringeElem))
    #priority, elem = fringe.get()
    #print (elem).heuristic

    #TODO: Need to think here, still not clear on the approach
    while not fringe.empty():
        successor(fringe.get())
            #priority, elem = s
            #if elem == goalState:
            #    return
            #heuristic = heuristicCalculator(s, goalState)
            #fringe.put(heuristic, s)
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
