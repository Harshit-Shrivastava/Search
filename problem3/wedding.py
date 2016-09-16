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

    return friends

if __name__ == "__main__":
    print(read_data())