"""
(1) Which search algorithm seems to work best for each routing options?
    -- Different algorithms perform better for each routing options.
        1. Segments:
        2. Distance:
        3. Time:
        4. Scenic:
(2) Which algorithm is fastest in terms of the amount of computation time
    required by your program, and by how much, according to your experiments?
    (To measure time accurately, you may want to temporarily include a loop in
    your program that runs the routing a few hundred or thousand times.)
    --
(3) Which algorithm requires the least memory, and by how much, according to
    your experiments?
    --
(4) Which heuristic function did you use, how good is it,
    and how might you make it better?
    --
(5) Supposing you start in Bloomington, which city should you travel to if
    you want to take the longest possible  drive (in miles) that is still the
    shortest path to that city? (In other words, which city is furthest from
    Bloomington?)
    --
"""
from algos import best_path
from utils_graph import build_graph
import sys


if __name__ == "__main__":
    start_city, end_city, routing_algorithm, routing_options = sys.argv[1:]
    graph, cities, max_limit = build_graph()
    result = best_path(graph, cities, routing_algorithm, start_city,
                     end_city, routing_options, max_limit)
    if result:
        print " ".join(str(i) for i in result[:2] if type(i) != str),  \
            " ".join(str(i) for i in result[3])
    else:
        print "Route not found. Please try other city."
