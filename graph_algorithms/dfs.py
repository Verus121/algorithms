from collections import deque

WHITE = "white" # undiscovered vertex
GREY = "grey" # discovered vertex
BLACK = "black" # explored vertex 

COLOR = 0
DISCOVERED = 1 # time first visited
EXPLORED = 2 # time all adj v visited 
PARENT = 3


def dfs_visit(adjacency_list, vertex_info, vertex, time):
    time += 1
    vertex_info[vertex][COLOR] = GREY
    vertex_info[vertex][DISCOVERED] = time

    for adj_vertex in adjacency_list[vertex]:
        if vertex_info[adj_vertex][COLOR] == WHITE:
            vertex_info[adj_vertex][PARENT] = vertex
            time = dfs_visit(adjacency_list, vertex_info, adj_vertex, time)
    
    time += 1
    vertex_info[vertex][COLOR] = BLACK
    vertex_info[vertex][EXPLORED] = time

    return time 


def dfs(adjacency_list, source):
    vertex_info = dict()
    time = 0
    
    for vertex in adjacency_list.keys():
        vertex_info[vertex] = [WHITE, -1, -1, None]
    
    dfs_visit(adjacency_list, vertex_info, source, time)
    print(vertex_info)


def main(): 
    # undirected graph G 
    adjacency_list = {
        "r": deque(["v", "s"]),
        "s": deque(["r", "w"]),
        "t": deque(["w", "x", "u"]),
        "u": deque(["t", "x", "y"]),
        "v": deque(["r"]),
        "w": deque(["s", "t", "x"]),
        "x": deque(["w", "t", "u", "y"]),
        "y": deque(["x", "u"]),
    }

    source = "s"

    dfs(adjacency_list, source)


main()
