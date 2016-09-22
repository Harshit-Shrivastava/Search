# This reads the input file and creates a square from the input by splitting between lines and spaces


def build_square(filename):
    square = []
    with open(filename) as file:
        lines = file.read().splitlines()
        for line in lines:
            square.append(line.split(' '))
    return square
