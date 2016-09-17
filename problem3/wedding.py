def read_data():
    friends = {}
    with open('myfriends.txt', 'r') as f:
        for line in f:
            friends[line.split()[0]] = set(line.split()[1:])
    temp = set(friends)
    for person in friends:
        temp = set(temp | friends[person])
    for value in temp:
        if value not in friends:
            friends[value] = set()
    for person in friends:
        for other_person in friends:
            if person != other_person:
                if person in friends[other_person]:
                    friends[person].add(other_person)
    return friends


def compute_neighbours(friends, seats_per_table):
    if seats_per_table < 1:
        return False
    elif seats_per_table == 1:
        return set(friends.keys())

    tentative_neighbours = {}
    # tentative stores all ppl who can b seated with a person
    for person in friends:
        tentative_neighbours[person] = set()
    for person in friends:
        for x in friends:
            if x != person and x not in friends[person]:
                tentative_neighbours[person].add(x)

    tables = {}
    i = 0
    for person in tentative_neighbours:
        tables[i] = set(person)
        # for neighbour in tentative_neighbours[person]:
            # if
        i += 1
    """tables = {}
    i=0
    for neighbour in tentative_neighbours:
        if len(tentative_neighbours[neighbour]) <= seats_per_table-1:
            print(tentative_neighbours[neighbour],neighbour)
            tables[i].add(tentative_neighbours[neighbour])
            tables[i].add(neighbour)
            i += 1

    print(tables)"""
    """for neighbour in tentative_neighbours:
        tables[i] = set(neighbour)
        for j in range( seats_per_table -1):
            n = list(neighbour)[j]
            tables[i].add( n )
            tentative_neighbours[neighbour].remove(n)
        i += 1"""
    # return tables
    return tentative_neighbours


if __name__ == "__main__":
    print(compute_neighbours(read_data(), 3))
