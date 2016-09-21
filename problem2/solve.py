import library
import sys
import copy

goalState = [['1','2','3','4'],['5','6','7','8'],['9','10','11','12'],['13','14','15','0']]


def move_left(i,j,curState):
    tempState1 = copy.deepcopy(curState)
    tempState1[i][j-1], tempState1[i][j] = tempState1[i][j], tempState1[i][j-1]
    return tempState1


def move_up(i,j,curState):
    tempState1 = copy.deepcopy(curState)
    tempState1[i][j], tempState1[i-1][j] = tempState1[i-1][j], tempState1[i][j]
    return tempState1


def move_down(i,j,curState):
    tempState1 = copy.deepcopy(curState)
    if i == 3:
        tempState1[i][j], tempState1[0][j] = tempState1[0][j], tempState1[i][j]
    else:
        tempState1[i][j], tempState1[i+1][j] = tempState1[i+1][j], tempState1[i][j]
    return tempState1


def move_right(i,j,curState):
    tempState1 = copy.deepcopy(curState)
    if j == 3:
        tempState1[i][0], tempState1[i][j] = tempState1[i][j], tempState1[i][0]
    else:
        tempState1[i][j+1], tempState1[i][j] = tempState1[i][j], tempState1[i][j+1]
    return tempState1


def successor(curStateObject):
    elem = curStateObject[1]
    curState = elem.state
    index = indexSearch(curState, '0')
    r = index[0]
    c = index[1]
    states = list()
    path1 = elem.path.copy()
    path1.append("D")
    states.append(library.FringeElement(move_down(r, c, curState),elem.costSoFar,elem.heuristic, path1))
    path2 = elem.path.copy()
    path2.append("L")
    states.append(library.FringeElement(move_left(r, c, curState),elem.costSoFar,elem.heuristic, path2))
    path3 = elem.path.copy()
    path3.append("U")
    states.append(library.FringeElement(move_up(r, c, curState),elem.costSoFar,elem.heuristic, path3))
    path4 = elem.path.copy()
    path4.append("R")
    states.append(library.FringeElement(move_right(r, c, curState),elem.costSoFar,elem.heuristic, path4))
    return states

def aStar(curSquare):
    heuristic = heuristicCalculator(curSquare, goalState)
    if (curSquare == goalState):
        return curSquare
    fringe = list()
    tempFringeElem = library.createElement(curSquare,0,heuristic,[])
    tempFringePri = library.fringePriority(tempFringeElem)
    fringe.append([tempFringePri, tempFringeElem])
    while len(fringe) > 0:
        min = float('inf')
        for element in fringe:
            if element[0] < min:
                min = element[0]
                minElement = element
        for s in successor(fringe.pop(fringe.index(minElement))):
            if s.state == goalState:
                return s.path
            s.costSoFar = s.costSoFar + 1
            s.heuristic = heuristicCalculator(s.state, goalState)
            tempFringePri = library.fringePriority(s)
            fringe.append([tempFringePri, s])
    return False

#function to find position of an element in an 2D list
def indexSearch(curState, elem):
    for row, i in enumerate(curState):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1

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