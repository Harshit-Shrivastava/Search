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