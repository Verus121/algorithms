

from numpy import Infinity
from sqlalchemy import true

PARENT = 0
SHORTEST_PATH_WEIGHT = 1 # estimate shortest path weight

def relax(edge, vertex_info):
    from_node, to_node, edge_weight = edge
    if vertex_info[from_node][SHORTEST_PATH_WEIGHT] + edge_weight < vertex_info[to_node][SHORTEST_PATH_WEIGHT]:
        vertex_info[to_node][PARENT] = from_node
        vertex_info[to_node][SHORTEST_PATH_WEIGHT] = vertex_info[from_node][SHORTEST_PATH_WEIGHT] + edge_weight
        return True
    return False

def bellman_ford(edge_list, vertex_info):
    vertices = len(vertex_info)
    for i in range(0, vertices - 1):
        for edge in edge_list:
            relax(edge, vertex_info)

    for edge in edge_list:
        if relax(edge, vertex_info):
            return False 
    return True 
        

def main():
    edge_list = [
        # [from, to, weight]
        ["s", "t", 6],
        ["s", "y", 7],
        ["t", "x", 5], 
        ["t", "z", -4], 
        ["t", "y", 8], 
        ["x", "t", -2], 
        ["y", "x", -3], 
        ["y", "z", 9], 
        ["z", "x", 7], 
        ["z", "s", 2], 
    ]

    vertex_info = dict()

    for edge in edge_list:
        vertex_info[edge[0]] = [None, Infinity] # parent, estimate shortest path weight

    source = "s"
    vertex_info[source] = [None, 0]

    if bellman_ford(edge_list, vertex_info):
        print(vertex_info)
    else:
        print("The Graph has a negative cycle")


main()