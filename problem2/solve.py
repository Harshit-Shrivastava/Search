def do(square, path):
    while path:
        move = path.pop(0)
        index = index_search(square, '0')
        if move == 'U':
            square = move_up(index[0], index[1], square)
        elif move == 'D':
            square = move_down(index[0], index[1], square)
        elif move == 'L':
            square = move_left(index[0], index[1], square)
        elif move == 'R':
            square = move_right(index[0], index[1], square)
    print(square)
