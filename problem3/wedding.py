def read_data():
    friends = {}
    with open('myfriends.txt', 'r') as f:
        for line in f:
            friends[line.split()[0]] = set(line.split()[1:])
    temp = set(friends)
    for person in friends:
        temp = set(temp |friends[person])
    for value in temp:
        if value not in friends:
            friends[value] = set()
    for person in friends:
        for other_person in friends:
            if person != other_person:
                if person in friends[other_person]:
                    friends[person].add(other_person)
    print(friends)
    return friends

def compute_neighbours(friends, seats_per_table):

    tentitive_neighbours = {}
    for person in friends:
        tentitive_neighbours[person] = set()
    for person in friends:
        for x in friends:
            if x not in friends[person] and x != person:
                print(x,person)
                tentitive_neighbours[person].add(x)
    ##tentitive stores all ppl who can b seated with a person
    ##somehow tentitive is coming wrong..please check if u have time

    """tables = {}
    i=0
    for neighbour in tentitive_neighbours:
        if len(tentitive_neighbours[neighbour]) <= seats_per_table-1:
            print(tentitive_neighbours[neighbour],neighbour)
            tables[i].add(tentitive_neighbours[neighbour])
            tables[i].add(neighbour)
            i += 1

    print(tables)"""
    """for neighbour in tentitive_neighbours:
        tables[i] = set(neighbour)
        for j in range( seats_per_table -1):
            n = list(neighbour)[j]
            tables[i].add( n )
            tentitive_neighbours[neighbour].remove(n)
        i += 1"""
    #return tables
    return tentitive_neighbours

if __name__ == "__main__":
    print(compute_neighbours(read_data(),3))