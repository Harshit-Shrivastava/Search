"""
Heuristic functions tried:-
1. No of tiles out of position
2. Sum of Manhattan distances of a tile from it's expected postion
3. Sum of Eucledian distance of a tile from it's expected postion

Manhattan distance works best as the heuristic function is much closer to the actual cost involved
in moving the tiles to their actual position. This makes sense as a tile can move only up(U), down(D),
left(L) or right(R), which is like moving as if we are in Manhattan and can move only in these directions.
"""

import sys
import copy
from math import sqrt


class FringeElement:
    def __init__(self, state, cost_so_far, heuristic, path):
        self.state = state
        self.cost_so_far = cost_so_far
        self.heuristic = heuristic
        self.path = path


# This reads the input file and creates a square from the input by splitting between lines and spaces
def build_square(filename):
    square = []
    with open(filename) as file:
        lines = file.read().splitlines()
        for line in lines:
            square.append(line.split(' '))
    return square


def move(i, j, cur_state, direction):
    temp_state1 = copy.deepcopy(cur_state)
    if direction == "l":
        temp_state1[i][j - 1], temp_state1[i][j] = temp_state1[i][j], temp_state1[i][j - 1]
    elif direction == "u":
        temp_state1[i][j], temp_state1[i - 1][j] = temp_state1[i - 1][j], temp_state1[i][j]
    elif direction == "d":
        if i == 3:
            temp_state1[i][j], temp_state1[0][j] = temp_state1[0][j], temp_state1[i][j]
        else:
            temp_state1[i][j], temp_state1[i + 1][j] = temp_state1[i + 1][j], temp_state1[i][j]
    elif direction == "r":
        if j == 3:
            temp_state1[i][0], temp_state1[i][j] = temp_state1[i][j], temp_state1[i][0]
        else:
            temp_state1[i][j + 1], temp_state1[i][j] = temp_state1[i][j], temp_state1[i][j + 1]
    return temp_state1


def successor(cur_state_object):
    elem = cur_state_object[1]
    cur_state = elem.state
    index = index_search(cur_state, '0')
    r = index[0]
    c = index[1]
    states = list()
    path1 = elem.path.copy()
    path1.append("D")
    states.append(FringeElement(move(r, c, cur_state, "d"), elem.cost_so_far, elem.heuristic, path1))
    path2 = elem.path.copy()
    path2.append("L")
    states.append(FringeElement(move(r, c, cur_state, "l"), elem.cost_so_far, elem.heuristic, path2))
    path3 = elem.path.copy()
    path3.append("U")
    states.append(FringeElement(move(r, c, cur_state, "u"), elem.cost_so_far, elem.heuristic, path3))
    path4 = elem.path.copy()
    path4.append("R")
    states.append(FringeElement(move(r, c, cur_state, "r"), elem.cost_so_far, elem.heuristic, path4))
    return states


# A-Star for finding solution to 15 puzzle problem
def a_star(cur_square):
    goal_state = [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12'], ['13', '14', '15', '0']]
    if cur_square == goal_state:
        return []
    heuristic = heuristic_calculator(FringeElement(cur_square, 0, 0, []), goal_state)
    fringe = list()
    temp_fringe_elem = FringeElement(cur_square, 0, heuristic, [])
    temp_fringe_pri = temp_fringe_elem.cost_so_far + temp_fringe_elem.heuristic
    fringe.append([temp_fringe_pri, temp_fringe_elem])
    visited = [cur_square]
    while len(fringe) > 0:
        min = float('inf')
        for element in fringe:
            if element[0] < min:
                min = element[0]
                min_element = element
        for s in successor(fringe.pop(fringe.index(min_element))):
            if s.state == goal_state:
                return s.path
            s.cost_so_far = s.cost_so_far + 1
            s.heuristic = heuristic_calculator(s, goal_state)
            temp_fringe_pri = s.cost_so_far + s.heuristic
            if s.state not in visited:
                visited.append(s.state)
            else:
                for i in range(len(fringe)):
                    if fringe[i][1].state == s.state and fringe[i][0] > temp_fringe_pri:
                        fringe.insert(i, [temp_fringe_pri, s])
                        break
                continue
            fringe.append([temp_fringe_pri, s])
    return False


# function to find position of an element in an 2D list
def index_search(cur_state, elem):
    for row, i in enumerate(cur_state):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1


# This function calculates the heuristic for the a-star algorithm
def heuristic_calculator(element, goal_state):
    heuristic = heuristic_helper(element.state, goal_state)
    index = index_search(element.state, "0")
    if len(element.path) == 0:
        return heuristic
    if index[0] == 0 and element.path[len(element.path) - 1] == 'U':
        square1 = copy.deepcopy(element.state)
        square1[0][index[1]], square1[3][index[1]] = square1[3][index[1]], square1[0][index[1]]
        temp_h = heuristic_helper(square1, goal_state)
        if temp_h < heuristic:
            heuristic = temp_h
    if index[1] == 0 and element.path[len(element.path) - 1] == 'L':
        square1 = copy.deepcopy(element.state)
        square1[0][index[1]], square1[3][index[1]] = square1[3][index[1]], square1[0][index[1]]
        temp_h = heuristic_helper(square1, goal_state)
        if temp_h < heuristic:
            heuristic = temp_h
    if index[0] == 3 and element.path[len(element.path) - 1] == 'D':
        square1 = copy.deepcopy(element.state)
        square1[index[0]][0], square1[index[0]][3] = square1[index[0]][3], square1[index[0]][0]
        temp_h = heuristic_helper(square1, goal_state)
        if temp_h < heuristic:
            heuristic = temp_h
    if index[1] == 3 and element.path[len(element.path) - 1] == 'R':
        square1 = copy.deepcopy(element.state)
        square1[index[0]][0], square1[index[0]][3] = square1[index[0]][3], square1[index[0]][0]
        temp_h = heuristic_helper(square1, goal_state)
        if temp_h < heuristic:
            heuristic = temp_h
    return heuristic


# heuristic - Manhattan distance
def heuristic_helper(square, goal_state):
    heuristic = 0
    for i in range(0, 4):
        for j in range(0, 4):
            temp = square[i][j]
            index = index_search(goal_state, temp)
            cur_manhattan_distance = abs(index[0] - i) + abs(index[1] - j)
            heuristic = heuristic + cur_manhattan_distance
    return heuristic


# heuristic  - Euclidean distance
def heuristic_helper_euclid(square, goal_state):
    heuristic = 0
    for i in range(0, 4):
        for j in range(0, 4):
            temp = square[i][j]
            index = index_search(goal_state, temp)
            cur_manhattan_distance = sqrt((index[0] - i) ** 2 + (index[1] - j) ** 2)
            heuristic = heuristic + cur_manhattan_distance
    return heuristic


# heuristic - number of displaced tiles
def heuristic_helper_displaced(square, goal_state):
    heuristic = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if square[i][j] != goal_state[i][j]:
                heuristic += 1
    return heuristic


# main Function
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid Input!")
    else:
        print(" ".join(a_star(build_square(sys.argv[1]))))
