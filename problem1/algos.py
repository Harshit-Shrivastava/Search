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
        return dfs_bfs(graph, start_city, end_city, routing_options, -1)
    elif algo.lower() == "bfs":
        return dfs_bfs(graph, start_city, end_city, routing_options, 0)
    elif algo.lower() == "ids":
        return ids(graph, start_city, end_city, routing_options)
    elif algo.lower() == "astar":
        return a_star(graph, start_city, end_city, routing_options)
    else:
        return False


def dfs_bfs(graph, start_city, end_city, routing_options, algo_flag):
    stack = [(start_city, [start_city])]
    visited = set()
    while stack:
        (city, path) = stack.pop(algo_flag)
        if city not in visited:
            if city == end_city:
                return path
            visited.add(city)
            for next_city in graph[city]:
                stack.append((next_city.end_city.name, path +  [
                    next_city.end_city.name]))


def ids(graph, start_city, end_city, routing_options):
    pass


def a_star(graph, start_city, end_city, routing_options):
    if (start_city == end_city):
        return [start_city]
    h = check(routing_options)
    fringe = []
    min = float('inf')
    for next_city in graph(start_city):
        if min > next_city.distance:
            min = next_city.distance
            min_city = next_city.end_city.name
        fringe.append(next_city.end_city.name,next_city.distance)

    return


def check(option):
    if option == "segments":
        return h_segments()
    elif option == "time":
        return h_time()
    elif option == "distance":
        return h_distance()
    elif option == "scenic":
        return h_scenic()
    else:
        return False


def h_segments():
    pass


def h_time():
    pass


def h_distance(cityA, cityB):
    pass


def h_scenic():
    pass