from math import sqrt


def aStar(square):
    heuristicCalculator(square)

#this function calculates the heuristic for the a-star algorithm
#heuristic is taken as the manhattan distance between the current position of the
def heuristicCalculator(square):
    heuristic = [[0]*4]*4
    for i in range(0,4):
        for j in range(0,4):
            if square[i][j] == 0:
                heuristic[i][j] = 0
            else:
                temp = int(square[i][j])
                temp_quo = temp / 4
                temp_rem = temp % 4
                #getting the row of the final position
                pos_i = temp_quo - 1
                #getting the column of the final position
                if temp_rem == 0:
                    pos_j = 3
                else:
                    pos_j = temp_rem - 1
                #calculating manhattan distance
                manhattan_distance = abs(pos_j - j) + abs(pos_i - i) - 1
                heuristic[i][j] = manhattan_distance
    print heuristic