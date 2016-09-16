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
    previous = []
    previous[start_city] = []
    if (start_city == end_city):
        return start_city
    path = []
    g_cost = []
    f_cost = []
    previous = []
    fringe = [start_city]
    g_cost[start_city] = 0
    f_cost[start_city] = heuristic(start_city,end_city,routing_options)
    while(fringe):
        min = float('inf')
        for city, cost in f_cost.items():
            if min > cost:
                min = cost
                min_city = city
        if (city == end_city):
            return [create_path(previous, city)]
        fringe.remove(city)
        path.append(city)
        for next_city in graph[city]:
            if next_city in path:
                continue
            temp = g_cost[city] + distance(city, next_city,graph)
            if next_city not in fringe:
                fringe.append(next_city)
            elif temp >= g_cost[next_city]:
                continue
            previous[next_city] = city
            g_cost[next_city] = temp
            f_cost[next_city] = g_cost[next_city] + heuristic(next_city,end_city,routing_options)

    return

def create_path(previous, city):
    path = [city]
    city = previous [city]
    for prev in previous:
        path.append(city)
        city = previous[prev]
    return path

def distance(cityA, cityB, graph):
    return graph[cityA][cityB].distance

def heuristic(start_city,end_city,routing_options):
    """
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
    """
    return
