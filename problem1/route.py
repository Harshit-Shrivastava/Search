"""
(1) Which search algorithm seems to work best for each routing options?
    -- Different algorithms perform better for each routing options.
    Segments: BFS will perform better because it will find least number of
    segments.
    Distance: A-star will perform better because it will find the less
    distance on
    heuristic.
    Time: BFS will perform better given the time constraint. A-star does not
    always perform better because the heuristic is distance based.
    Scenic: DFS will perform better in this case.

(2) Which algorithm is fastest in terms of the amount of computation time
    required by your program, and by how much, according to your experiments?
    (To measure time accurately, you may want to temporarily include a loop in
    your program that runs the routing a few hundred or thousand times.)

    Ran the algorithm within a loop for 100 times.
    -- A-star algorithm takes 1194ms for Carson,_California to Bloomington,
    Indiana Whereas bfs takes 14343ms, dfs takes 51359ms and IDS takes the
    most time
    A-star is 8~12 times faster than BFS
    A-star is 30~40 times faster than DFS
    A-star is more than 100 to 1000 times faster than IDS.

(3) Which algorithm requires the least memory, and by how much, according to
    your experiments?

    -- Memory stats: (Bloomington, Indiana to Toronto,_Ontario)
    DFS takes the least memory. Since there is less branching factor at every
    level there is only one node stored in the fringe at every depth. Whereas
    BFS stores all of the branches and takes > 0.3MB of data for fringe
    compared to DFS. IDS stores depth + the node of each branch at that level.
    A-star consumes lot of space because we're using open set and closed set
    with the fringe at every level.

(4) Which heuristic function did you use, how good is it,
    and how might you make it better?

    -- We used the distance between 2 coordinates as our heuristic for
    routing_options=distance. This was calculated using the haversine-formula.
    It is always less than or equal to the distance between 2 cities via any
    path. It is fairly good for routes which have less number of
    intersections connected. It can be made better by including

        1. The direction sense in it and by giving points. Consider if we
        are moving towards the end city then we can give +ve points and -ve for
        moving away.
        2. If given information on city latitude and longitude or more
        information on the intersection then we can use heuristic better.

(5) Supposing you start in Bloomington, which city should you travel to if
    you want to take the longest possible  drive (in miles) that is still the
    shortest path to that city? (In other words, which city is furthest from
    Bloomington?)

    -- Skagway, Alaska is the farthest from Bloomington. To take the longest
    possible drive (in miles), one should travel to Skagway, Alaska from
    Bloomington for 5814 miles according to the given data.

"""
import sys
from math import radians, cos, sin, asin, sqrt
"""
routing_options =
- segments finds a route with the fewest number of \turns"
    (i.e. edges of the graph)
- distance finds a route with the shortest total distance
- time finds the fastest route, for a car that always travels at the speed limit
- scenic finds the route having the least possible distance spent on highways
    (which we define as roads with speed limits 55 mph or greater)
"""


def build_graph():
    # Graph = { "A" (str) :  List(Segments Connected to A), ...... }
    # A (City) = name, lat, long, adjacency list
    # Cities = { "A" (str) : city object }
    graph = {}
    cities = {}
    max_limit = 0
    with open('road-segments.txt', 'r') as f:
        for line in f:
            temp = line.split(' ')
            str_city_a = temp[0]
            str_city_b = temp[1]
            city_a = City(str_city_a)
            city_b = City(str_city_b)
            seg_a = add_segment(city_b, temp[2], temp[3], temp[4])
            seg_b = add_segment(city_a, temp[2], temp[3], temp[4])
            try:
                limit = int(temp[3])
            except ValueError:
                limit = int(1)
            if limit > max_limit:
                max_limit = limit

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
    with open('city-gps.txt', 'r') as f:
        for line in f:
            temp = line.split(' ')
            if temp[0] not in cities:
                cities[temp[0]] = City(temp[0])
            cities[temp[0]].lat = temp[1]
            cities[temp[0]].long = temp[2]
    return graph, cities, max_limit


def convert2int(a):
    try:
        x = int(a)
        return x
    except ValueError:
        return -1


def add_segment(cityB, distance, limit, highway):
    return Segment(cityB, distance, limit, highway)


class Segment:

    def __init__(self, end_city, distance, limit, highway):
        self.end_city = end_city
        self.distance = convert2int(distance)
        self.limit = convert2int(limit)
        self.highway = highway


class City:

    def __init__(self, name, latitude=0, longitude=0):
        self.name = name
        self.lat = latitude
        self.long = longitude

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        # return self.name == other.name
        return self.name == other


def best_path(graph, cities, algo, start_city, end_city, routing_options, max_limit):
    if algo.lower() == "dfs":
        path = dfs_bfs(graph, start_city, end_city, routing_options, -1)
    elif algo.lower() == "bfs":
        path = dfs_bfs(graph, start_city, end_city, routing_options, 0)
    elif algo.lower() == "ids":
        path = ids(graph, start_city, end_city, routing_options)
    elif algo.lower() == "astar":
        path = a_star(graph, cities, start_city, end_city, routing_options, max_limit)
    else:
        return False
    if path is not None:
        return calc_distance(path, graph), abs(calc_time(path, graph)), \
               calc_seg(
            path), path
    else:
        return False


def dfs_bfs(graph, start_city, end_city, routing_options, algo_option):
    stack = [(start_city, [start_city])]
    visited = set()
    while stack:
        (city, path) = stack.pop(algo_option)
        if city not in visited:
            if city == end_city:
                return path
            temp_stack = []
            visited.add(city)
            for next_city in graph[city]:
                temp_cost = cost(graph, city, next_city.end_city.name,
                                 routing_options)
                temp_stack.append((next_city.end_city.name, path+[
                    next_city.end_city.name], temp_cost))
            # At each level get the cost from option and sort based on cost.
            if algo_option == 0:
                # BFS Sort in the right order for stack to pick up.
                temp_stack.sort(key=lambda x: x[2])
            else:
                # DFS Sort in reverse order for stack to pick up.
                temp_stack.sort(key=lambda x: x[2], reverse=True)
            temp_stack = [(i, j) for i, j, k in temp_stack]
            stack.extend(temp_stack)


def ids(graph, start_city, end_city, routing_options):
    i = 0
    while True:
        visited = dict()
        stack = [(start_city, [start_city])]
        while stack:
            (city, path) = stack.pop(-1)
            depth = len(path)
            if city not in visited.keys():
                if city == end_city:
                    return path
                visited[city] = depth
                if depth > i:
                    continue
                temp_stack = []
                for next_city in graph[city]:
                    temp_cost = cost(graph, city, next_city.end_city.name,
                                     routing_options)
                    temp_stack.append((next_city.end_city.name, path + [
                        next_city.end_city.name], temp_cost))
                temp_stack.sort(key=lambda a: a[2], reverse=True)
                temp_stack = [(x, y) for x, y, z in temp_stack]
                stack.extend(temp_stack)
            elif visited[city] > depth:
                stack.append((city, path))
                visited.pop(city)
        i += 1


def a_star(graph, cities, start_city, end_city, routing_options, max_limit):
    if start_city == end_city:
        return [start_city]
    path = list()
    fringe = list()
    fringe.append(start_city)
    g = dict()
    f = dict()
    g[start_city] = 0
    f[start_city] = heuristic(cities, start_city, end_city, graph)
    while len(fringe) > 0:
        min_cost = float('Inf')
        # curr = fringe.pop(0)
        for fx in f:
            if fx in fringe and f[fx] < min_cost:
                min_cost = f[fx]
                curr = fx
        if curr == end_city:
            path.append(curr)
            return path
        fringe.remove(curr)
        path.append(curr)
        temp_list = []
        for neighbour in graph[curr]:
            if neighbour.end_city.name not in path:
                if neighbour.end_city.name not in fringe:
                    temp_cost = cost(graph, curr, neighbour.end_city.name,
                                     routing_options)
                    g[neighbour.end_city.name] = temp_cost
                    f[neighbour.end_city.name] = g[neighbour.end_city.name] +\
                                                 heuristic(cities, neighbour.end_city.name, end_city, graph)
                    temp_list.append((neighbour.end_city.name,
                                      f[neighbour.end_city.name]))
        temp_list.sort(key=lambda a: a[1])
        temp_list = [x for x, y in temp_list]
        fringe.extend(temp_list)
    return False


def create_path(previous, curr):
    path = [curr]
    while curr in previous:
        curr = previous[curr]
        path.append(curr)
    return path[::-1]


def cost(graph, start_city, end_city, routing_options):
    if routing_options == "segments":
        return 1
    elif routing_options == "time":
        for seg in graph[start_city]:
            if seg.end_city == end_city:
                if seg.limit != 0:
                    return (seg.distance * 1.0)/seg.limit
                return seg.distance
    elif routing_options == "distance":
        for seg in graph[start_city]:
            if seg.end_city == end_city:
                return seg.distance
    elif routing_options == "scenic":
        for seg in graph[start_city]:
            if seg.end_city == end_city:
                if seg.limit >= 55:
                    return 2
                else:
                    return 1
    else:
        return False
    return False


def heuristic(cities, start_city, end_city, graph):
    distance_ = get_distance(start_city, cities, end_city, graph)
    if distance_ is None:
        distance_ = 0
    return distance_


def get_distance(start_city, cities, end_city, graph):
    if check_lat_long(start_city, cities):
        return distance(cities[start_city].lat, cities[start_city].long,
                        cities[end_city].lat, cities[end_city].long)
    else:
        temp = get_city(start_city, graph, cities)
        if temp:
            return distance(cities[temp[1].end_city.name].lat, cities[
                temp[1].end_city.name].long,
                            cities[end_city].lat, cities[end_city].long) \
                   + temp[1].distance


def get_city(city, graph, cities):
    for neighbour in graph[city]:
        if check_lat_long(neighbour.end_city.name, cities):
            return city, neighbour
    return False


def check_lat_long(city, cities):
    if cities[city].lat == 0 or cities[city].long == 0:
        return False
    return True


# haversine formula for distance
def distance(lat1, lon1, lat2, lon2):
    lat1 = radians(float(lat1))
    lat2 = radians(float(lat2))
    lon1 = radians(float(lon1))
    lon2 = radians(float(lon2))

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 3956  # Radius of earth 3956 miles
    return c * r


def calc_distance(path, graph):
    dist = 0
    for i in range(len(path)-1):
        for city in graph[path[i]]:
            if city.end_city.name == path[i+1]:
                dist = dist + city.distance
                break
    return dist


def calc_time(path, graph):
    time = 0
    for i in range(len(path)-1):
        for city in graph[path[i]]:
            if city.end_city.name == path[i+1]:
                if city.limit != 0:
                    time += (city.distance*1.0/city.limit)
                break
    return round(time, 4)


def calc_seg(path):
    return len(path) - 1


if __name__ == "__main__":
    start_city, end_city, routing_options, routing_algorithm = sys.argv[1:]
    graph, cities, max_limit = build_graph()
    result = []
    result = best_path(graph, cities, routing_algorithm, start_city,
                       end_city, routing_options, max_limit)
    if result:
        print " ".join(str(i) for i in result[:2] if type(i) != str),  \
            " ".join(str(i) for i in result[3])
    else:
        print "Route not found. Please try other city."
