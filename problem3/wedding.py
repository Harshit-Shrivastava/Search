import itertools


def load_data(file_name):
    friends = {}
    everyone = set([])
    with open(file_name, 'r') as f:
        for line in f:
            line_list = line.split()
            if line_list[0] in friends:
                friends[line_list[0]].update(set(line_list[1:]))
            else:
                friends[line_list[0]] = set(line_list[1:])
            for i in line_list[1:]:
                if i not in friends:
                    friends[i] = set([line_list[0]])
                else:
                    friends[i].update(set([line_list[0]]))
            everyone.update(set(line.split()))
    return everyone, friends


def transpose(friends_graph, everyone):
    new_graph = {}
    for i in friends_graph:
        new_graph[i] = everyone.difference(friends_graph[i] | set([i]))
    return new_graph


def printable(states):
    print len(states), " ".join(",".join(j for j in i) for i in states)


# Should generate only certain number of valid states.
def successors(state, friends_graph_t):
    return [[[i] for i in friends_graph_t]]


def generate_states(initial_state, everyone, friends_graph_t):
    fringe = [initial_state]
    optimal = [-1, []]
    while len(fringe) > 0:
        state = fringe.pop()
        for s in successors(state, friends_graph_t):
            temp = len(s)
            if optimal[0] == -1 or optimal[0] > temp:
                optimal[0] = temp
                optimal[1] = s
            fringe.append(s)
        break
    return optimal


if __name__ == "__main__":
    seats_per_table = 2
    file_name = 'myfriends.txt'
    everyone, friends_graph = load_data(file_name)
    friends_graph_t = transpose(friends_graph, everyone)
    initial_state = [[]]
    printable(generate_states(initial_state, everyone, friends_graph_t)[1])
