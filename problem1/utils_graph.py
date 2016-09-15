from libraries import City, add_segment


def build_graph():
    # Graph = { "A" (str) :  List(Segments Connected to A), ...... }
    # A (City) = name, lat, long, adjacency list
    # Cities = { "A" (str) : city object }
    graph = {}
    cities = {}
    with open('road-segments.txt', 'r') as f:
        for line in f:
            temp = line.split(' ')
            str_city_a = temp[0]
            str_city_b = temp[1]
            city_a = City(str_city_a)
            city_b = City(str_city_b)
            seg_a = add_segment(city_a, city_b, temp[2], temp[3], temp[4])
            seg_b = add_segment(city_b, city_a, temp[2], temp[3], temp[4])

            # Add to Cities Hash
            if str_city_a not in cities:
                cities[str_city_a] = city_a
            if str_city_b not in cities:
                cities[str_city_b] = city_b

            # Add to Graph Hash
            # We can replace this step where we can use Object Key but:
            # 1. We can't reconstruct the same object to check if the key is
            # present.
            # 2. It will be an extra step to get the object name from other
            # hash table. Instead we can use a string where it can be easily
            # debugged.
            if str_city_a in graph:
                graph[str_city_a].append(seg_a)
            else:
                graph[str_city_a] = [seg_a]
            if str_city_b in graph:
                graph[str_city_b].append(seg_b)
            else:
                graph[str_city_b] = [seg_b]
    return graph, cities
