def dfs(graph,cities,start_city, end_city, routing_options):
    """s_city = start_city
    e_city = end_city
    path = []
    if start_city not in graph or end_city not in graph:
        return False
    fringe =[start_city]
    path.append(start_city)
    for city in graph[fringe.pop()]:
        path.append(city.name)
        if city.name == end_city:
            return path
            fringe.append(city)
        path.pop()
    """
    return dfs_helper(graph,cities,start_city, end_city, routing_options,[])

def dfs_helper(graph,cities,start_city, end_city, routing_options,path):
    path.append(start_city)
    if start_city == end_city:
        return path
    for seg in graph[start_city]:
        if end_city not in path and seg.end_city.name not in path:
            dfs_helper(graph,cities,seg.end_city.name, end_city, routing_options,path)
    return path