from math import sqrt
import library
import sys
import copy


def move_left(i, j, cur_state):
    temp_state1 = copy.deepcopy(cur_state)
    temp_state1[i][j-1], temp_state1[i][j] = temp_state1[i][j], temp_state1[i][j-1]
    return temp_state1


def move_up(i, j, cur_state):
    temp_state1 = copy.deepcopy(cur_state)
    temp_state1[i][j], temp_state1[i-1][j] = temp_state1[i-1][j], temp_state1[i][j]
    return temp_state1


def move_down(i, j, cur_state):
    temp_state1 = copy.deepcopy(cur_state)
    if i == 3:
        temp_state1[i][j], temp_state1[0][j] = temp_state1[0][j], temp_state1[i][j]
    else:
        temp_state1[i][j], temp_state1[i+1][j] = temp_state1[i+1][j], temp_state1[i][j]
    return temp_state1


def move_right(i, j, cur_state):
    temp_state1 = copy.deepcopy(cur_state)
    if j == 3:
        temp_state1[i][0], temp_state1[i][j] = temp_state1[i][j], temp_state1[i][0]
    else:
        temp_state1[i][j+1], temp_state1[i][j] = temp_state1[i][j], temp_state1[i][j+1]
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
    states.append(library.FringeElement(move_down(r, c, cur_state), elem.cost_so_far, elem.heuristic, path1))
    path2 = elem.path.copy()
    path2.append("L")
    states.append(library.FringeElement(move_left(r, c, cur_state), elem.cost_so_far, elem.heuristic, path2))
    path3 = elem.path.copy()
    path3.append("U")
    states.append(library.FringeElement(move_up(r, c, cur_state), elem.cost_so_far, elem.heuristic, path3))
    path4 = elem.path.copy()
    path4.append("R")
    states.append(library.FringeElement(move_right(r, c, cur_state), elem.cost_so_far, elem.heuristic, path4))
    return states

def do(square, path):
    while path:
        move = path.pop(0)
        index = index_search(square, '0')
        if move == 'U':
            square = move_up(index[0],index[1],square)
        elif move == 'D':
            square = move_down(index[0],index[1],square)
        elif move == 'L':
            square = move_left(index[0], index[1], square)
        elif move == 'R':
            square = move_right(index[0],index[1],square)
    print(square)


def a_star(cur_square):
    goal_state = [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['9', '10', '11', '12'], ['13', '14', '15', '0']]
    if cur_square == goal_state:
        return cur_square
    heuristic = heuristic_calculator(library.create_element(cur_square, 0, 0, []), goal_state)
    fringe = list()
    temp_fringe_elem = library.create_element(cur_square, 0, heuristic, [])
    temp_fringe_pri = library.fringe_priority(temp_fringe_elem)
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
            temp_fringe_pri = library.fringe_priority(s)
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


# this function calculates the heuristic for the a-star algorithm
def heuristic_calculator(element, goal_state):
    heuristic = heuristic_helper(element.state, goal_state)
    index = index_search(element.state, "0")
    if len(element.path) == 0:
        return heuristic
    if index[0] == 0 and element.path[len(element.path)-1] == 'U':
        square1 = copy.deepcopy(element.state)
        square1[0][index[1]], square1[3][index[1]] = square1[3][index[1]], square1[0][index[1]]
        temp_h = heuristic_helper(square1, goal_state)
        if temp_h < heuristic:
            heuristic = temp_h
    if index[1] == 0 and element.path[len(element.path)-1] == 'L':
        square1 = copy.deepcopy(element.state)
        square1[0][index[1]], square1[3][index[1]] = square1[3][index[1]], square1[0][index[1]]
        temp_h = heuristic_helper(square1, goal_state)
        if temp_h < heuristic:
            heuristic = temp_h
    if index[0] == 3 and element.path[len(element.path)-1] == 'D':
        square1 = copy.deepcopy(element.state)
        square1[index[0]][0], square1[index[0]][3] = square1[index[0]][3], square1[index[0]][0]
        temp_h = heuristic_helper(square1, goal_state)
        if temp_h < heuristic:
            heuristic = temp_h
    if index[1] == 3 and element.path[len(element.path)-1] == 'R':
        square1 = copy.deepcopy(element.state)
        square1[index[0]][0], square1[index[0]][3] = square1[index[0]][3], square1[index[0]][0]
        temp_h = heuristic_helper(square1, goal_state)
        if temp_h < heuristic:
            heuristic = temp_h
    return heuristic


# heuristic is taken as the manhattan distance between the current position of the
def heuristic_helper(square, goal_state):
    heuristic = 0
    for i in range(0, 4):
        for j in range(0, 4):
            temp = square[i][j]
            index = index_search(goal_state, temp)
            cur_manhattan_distance = abs(index[0] - i) + abs(index[1] - j)
            heuristic = heuristic + cur_manhattan_distance
    return heuristic


def heuristic_helper_euclid(square, goal_state):
    heuristic = 0
    for i in range(0, 4):
        for j in range(0, 4):
            temp = square[i][j]
            index = index_search(goal_state, temp)
            cur_manhattan_distance = sqrt((index[0] - i)**2 + (index[1] - j)**2)
            heuristic = heuristic + cur_manhattan_distance
    return heuristic


def heuristic_helper_displaced(square, goal_state):
    heuristic = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if square[i][j] != goal_state[i][j]:
                heuristic += 1
    return heuristic


def heuristic_helper_displaced_dist(square, goal_state):
    heuristic = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if square[i][j] != goal_state[i][j]:
                heuristic += 1
    return heuristic
