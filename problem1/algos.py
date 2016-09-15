"""
routing_options =
- segments finds a route with the fewest number of \turns" (i.e. edges of the graph)
- distance finds a route with the shortest total distance
- time finds the fastest route, for a car that always travels at the speed limit
- scenic finds the route having the least possible distance spent on highways (which we define
as roads with speed limits 55 mph or greater)
"""

def best_path(graph, algo, start_city, end_city, routing_options):
    if algo.lower() == "dfs":
        return dfs(graph, start_city, end_city, routing_options);
    elif algo.lower() == "bfs":
        return bfs(graph, start_city, end_city, routing_options);
    elif algo.lower() == "ids":
        return ids(graph, start_city, end_city, routing_options);
    elif algo.lower() == "astar":
        return a_star(graph, start_city, end_city, routing_options);
    else:
        return False

def dfs(graph, start_city, end_city, routing_options):
    stack = [(start_city, [start_city])]
    visited = set()
    while stack:
        (city, path) = stack.pop()
        if city not in visited:
            if city == end_city:
                return path
            visited.add(city)
            for next_city in graph[city]:
                stack.append((next_city.end_city.name, path + [next_city.end_city.name]))

def bfs(graph, start_city, end_city, routing_options):
    return

def ids(graph, start_city, end_city, routing_options):
    return

def a_star(graph, start_city, end_city, routing_options):
    if (start_city == end_city):
        return [start_city]
    h = 0
    if routing_options == "segments":
        h = h_segments()
    elif routing_options == "time":
        h = h_time()
    elif routing_options == "distance":
        h = h_distance()
    elif routing_options == "scenic":
        h = h_scenic()
    else:
        return False
    fringe = []
    min = float('inf')
    for next_city in graph(start_city):
        if min > next_city.distance:
            min = next_city.distance
            min_city = next_city.end_city.name
        fringe.append(next_city.end_city.name,next_city.distance)

    return

def h_segments():
    return

def h_time():
    return

def h_distance(cityA, cityB):

    return

def h_scenic():
    return