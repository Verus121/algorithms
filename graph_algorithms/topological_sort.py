# Directed Acyclic Graph 

from collections import deque

WHITE = "white" # undiscovered vertex
GREY = "grey" # discovered vertex
BLACK = "black" # explored vertex 

COLOR = 0
PARENT = 1


def dfs_visit(vertex, graph, vertex_info, topological_ordering):
    vertex_info[vertex][COLOR] = GREY

    for adj_vertex in graph[vertex]:
        if vertex_info[adj_vertex][COLOR] == WHITE:
            vertex_info[adj_vertex][PARENT] = vertex
            dfs_visit(adj_vertex, graph, vertex_info, topological_ordering)
    
    vertex_info[vertex][COLOR] = BLACK
    topological_ordering.appendleft(vertex)


def main():
    graph = {
        "A": ["D"], 
        "B": ["D"], 
        "C": ["A", "B"],
        "D": ["H", "G"], 
        "E": ["A", "D", "F"],
        "F": ["K", "J"],
        "G": ["I"],
        "H": ["J", "I"], 
        "I": ["L"],
        "J": ["M", "L"], 
        "K": ["J"],
        "L": [],
        "M": [],
    }
    topological_ordering = deque()

    vertex_info = dict()
    for vertex in graph.keys():
        vertex_info[vertex] = [WHITE, None]
    
    for vertex in graph.keys():
        if vertex_info[vertex][COLOR] == WHITE:
            dfs_visit(vertex, graph, vertex_info, topological_ordering)
    
    print(topological_ordering)

main() 