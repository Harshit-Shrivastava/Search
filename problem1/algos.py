"""
routing_options =
- segments finds a route with the fewest number of \turns"
    (i.e. edges of the graph)
- distance finds a route with the shortest total distance
- time finds the fastest route, for a car that always travels at the speed limit
- scenic finds the route having the least possible distance spent on highways
    (which we define as roads with speed limits 55 mph or greater)
"""
from math import radians, cos, sin, asin, sqrt


def best_path(graph, cities, algo, start_city, end_city, routing_options):
    if algo.lower() == "dfs":
        path = dfs_bfs(graph, start_city, end_city, routing_options, -1)
    elif algo.lower() == "bfs":
        path = dfs_bfs(graph, start_city, end_city, routing_options, 0)
    elif algo.lower() == "ids":
        path = ids(graph, cities, start_city, end_city, routing_options)
    elif algo.lower() == "astar":
        path = a_star(graph, cities, start_city, end_city, routing_options)
    else:
        return False
    return calc_distance(path, graph), calc_time(path, graph), calc_seg(
        path), path


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


def ids(graph, cities, start_city, end_city, routing_options):
    i = 0
    while True:
        visited = dict()
        stack = [(start_city, [start_city])]
        while stack:
            (city, path) = stack.pop(0)
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
                temp_stack.sort(key=lambda x: x[2])
                temp_stack = [(i, j) for i, j, k in temp_stack]
                stack.extend(temp_stack)
            elif visited[city] > depth:
                stack.append((city, path))
                visited.pop(city)
        i += 1


def a_star(graph, cities, start_city, end_city, routing_options):
    if start_city == end_city:
        return [start_city]
    path = set()
    fringe = set()
    fringe.add(start_city)
    previous = dict()
    g = dict()
    f = dict()
    g[start_city] = 0
    f[start_city] = heuristic(cities, start_city, end_city, routing_options)
    while len(fringe) > 0:
        min_cost = float('Inf')
        for fx in f:
            if fx in fringe and f[fx] < min_cost:
                min_cost = f[fx]
                curr = fx
        if curr == end_city:
            return create_path(previous, curr)
        fringe.remove(curr)
        path.add(curr)
        for neighbour in graph[curr]:
            if neighbour.end_city.name not in path:
                tentative_cost = g[curr] + cost(graph, curr, neighbour.end_city.name, routing_options)
                if neighbour.end_city.name not in fringe:
                    fringe.add(neighbour.end_city.name)
                elif tentative_cost >= g[neighbour.end_city.name]:
                    continue
                previous[neighbour.end_city.name] = curr
                g[neighbour.end_city.name] = tentative_cost
                f[neighbour.end_city.name] = g[neighbour.end_city.name] + heuristic(cities, neighbour.end_city.name,
                                                                                    end_city, routing_options)
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


def heuristic(cities, start_city, end_city, routing_options):
    if routing_options == "segments":
        return distance(cities[start_city].lat, cities[start_city].long, cities[end_city].lat, cities[end_city].long)
    elif routing_options == "time":
        return distance(cities[start_city].lat, cities[start_city].long, cities[end_city].lat, cities[end_city].long)
    elif routing_options == "distance":
        return distance(cities[start_city].lat, cities[start_city].long, cities[end_city].lat, cities[end_city].long)
    elif routing_options == "scenic":
        return distance(cities[start_city].lat, cities[start_city].long, cities[end_city].lat, cities[end_city].long)
    else:
        return False


# http://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula
def distance(lat1, lon1, lat2, lon2):
    lat1 = radians(float(lat1))
    lat2 = radians(float(lat2))
    lon1 = radians(float(lon1))
    lon2 = radians(float(lon2))

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 3956  # Radius of earth 3956 miles
    return c * r

    # if we find the equation of the line betwn strt n end
    # then whatever city is on the line
    # acc to that heuristic of min no of edges can b found


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
