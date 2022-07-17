from cmath import inf
from collections import deque
from numpy import Infinity 


WHITE = "white" # undiscovered vertex
GREY = "grey" # discovered vertex
BLACK = "black" # explored vertex 

COLOR = 0
DISTANCE = 1
PARENT = 2

def bfs(adjacency_list, source):
    vertex_info = dict()
    queue = deque() # add to queue with append(el), remove from queue with popleft(). 

    for vertex in adjacency_list.keys():
        if vertex == source:
            vertex_info[vertex] = [GREY, 0, None]
        else:
            vertex_info[vertex] = [WHITE, -1, None]

    queue.append(source)

    while len(queue) != 0:
        vertex = queue.popleft()
        for adj_vertex in adjacency_list[vertex]:
            if vertex_info[adj_vertex][COLOR] == WHITE:
                vertex_info[adj_vertex][COLOR] = GREY
                vertex_info[adj_vertex][DISTANCE] = vertex_info[vertex][DISTANCE] + 1
                vertex_info[adj_vertex][PARENT] = vertex
                queue.append(adj_vertex)

        vertex_info[vertex][COLOR] = BLACK
    
    for vertex, info in vertex_info.items():
        print(vertex, info)
        
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

    bfs(adjacency_list, source)


main()
