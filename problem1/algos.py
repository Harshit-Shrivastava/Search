"""
routing_options =
- segments finds a route with the fewest number of \turns" (i.e. edges of the graph)
- distance finds a route with the shortest total distance
- time finds the fastest route, for a car that always travels at the speed limit
- scenic finds the route having the least possible distance spent on highways (which we define
as roads with speed limits 55 mph or greater)
"""
from math import radians, cos, sin, asin, sqrt


def best_path(graph, cities, algo, start_city, end_city, routing_options):
    if algo.lower() == "dfs":
        return dfs_bfs(graph, cities, start_city, end_city, routing_options, -1)
    elif algo.lower() == "bfs":
        return dfs_bfs(graph, cities, start_city, end_city, routing_options, 0)
    elif algo.lower() == "ids":
        return ids(graph, cities, start_city, end_city, routing_options)
    elif algo.lower() == "astar":
        return a_star(graph, cities, start_city, end_city, routing_options)
    else:
        return False


def dfs_bfs(graph, cities, start_city, end_city, routing_options, algo_flag):
    stack = [(start_city, [start_city])]
    visited = set()
    while stack:
        (city, path) = stack.pop(algo_flag)
        if city not in visited:
            if city == end_city:
                return path
            visited.add(city)
            for next_city in graph[city]:
                stack.append((next_city.end_city.name, path + [
                    next_city.end_city.name]))


def ids(graph, cities, start_city, end_city, routing_options):
    i = 0
    while True:
        visited = set()
        stack = [(start_city, [start_city])]
        while stack:
            (city, path) = stack.pop()
            depth = len(path)
            if city not in visited:
                if city == end_city:
                    return path
                visited.add(city)
                if depth > i:
                    continue
                for next_city in graph[city]:
                    stack.append((next_city.end_city.name, path + [
                        next_city.end_city.name]))
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
    return path


def cost(graph, start_city, end_city, routing_options):
    if routing_options == "segments":
        return False
    elif routing_options == "time":
        return False
    elif routing_options == "distance":
        for seg in graph[start_city]:
            if seg.end_city == end_city:
                return seg.distance
    elif routing_options == "scenic":
        return False
    else:
        return False
    return False


def heuristic(cities, start_city, end_city, routing_options):
    if routing_options == "segments":
        return False
    elif routing_options == "time":
        return False
    elif routing_options == "distance":
        return distance(cities[start_city].lat, cities[start_city].long, cities[end_city].lat, cities[end_city].long)
    elif routing_options == "scenic":
        return False
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
    r = 3956  # Radius of earth 6371 for kilometers. 3956 for miles
    return c * r
