# from numpy import transpose

WHITE = "white" # undiscovered vertex
GREY = "grey" # discovered vertex
BLACK = "black" # explored vertex 

COLOR = 0
DISCOVERED = 1 # time first visited
EXPLORED = 2 # time all adj v visited 
PARENT = 3
T_PARENT = 1


def get_graph_transpose(graph):
    transpose_graph = dict()

    for vector in graph:
        transpose_graph[vector] = list()

    for vector in graph:
        for value in graph[vector]:
            transpose_graph[value].append(vector)
    
    return transpose_graph


def dfs_visit(graph, dfs_info, vertex, time):
    time += 1
    dfs_info[vertex][COLOR] = GREY
    dfs_info[vertex][DISCOVERED] = time

    for adj_vertex in graph[vertex]:
        if dfs_info[adj_vertex][COLOR] == WHITE:
            dfs_info[adj_vertex][PARENT] = vertex
            time = dfs_visit(graph, dfs_info, adj_vertex, time)
    
    time += 1
    dfs_info[vertex][COLOR] = BLACK
    dfs_info[vertex][EXPLORED] = time

    return time 


def graph_dfs(graph):
    dfs_info = dict() 
    time = 0

    for vertex in graph.keys():
        dfs_info[vertex] = [WHITE, -1, -1, None] # COLOR, DISCOVER, EXPLORED, PARENT

    for vertex in graph.keys():
        if dfs_info[vertex][COLOR] == WHITE:
            time = dfs_visit(graph, dfs_info, vertex, time)

    return dfs_info


def get_reverse_explored(dfs_info):

    explored_time_list = list()
    for vertex in dfs_info:
        explored_time = dfs_info[vertex][EXPLORED]
        explored_time_list.append(explored_time)

    explored_time_list.sort(reverse=True)

    explored_vertex_list = list()
    for explored_time in explored_time_list:
        vertex_of_explored_time = None
        for vertex in dfs_info.keys():
            if dfs_info[vertex][EXPLORED] == explored_time:
                vertex_of_explored_time = vertex

        explored_vertex_list.append(vertex_of_explored_time)
    
    return explored_vertex_list



def transpose_graph_dfs(transpose_graph, reverse_explored):
    dfs_info = dict()

    for vertex in transpose_graph.keys():
        dfs_info[vertex] = [WHITE, None] # COLOR, DISCOVER, EXPLORED, PARENT

    for vertex in transpose_graph.keys():
        if dfs_info[vertex][COLOR] == WHITE:
            transpose_graph_dfs_visit(transpose_graph, dfs_info, vertex)

    return dfs_info
    



def main():
    graph = {
        "A": ["B", "E"], 
        "B": ["F"], 
        "C": ["B", "D", "G"],
        "D": ["G"], 
        "E": ["A", "F"],
        "F": ["C", "G"],
        "G": ["H"],
        "H": ["D"], 
    }
    print(graph)

    transpose_graph = get_graph_transpose(graph)
    print(transpose_graph)

    dfs_info = graph_dfs(graph)
    print(dfs_info)

    reverse_explored = get_reverse_explored(dfs_info)
    print(reverse_explored)

    transpose_graph_dfs(transpose_graph, reverse_explored)


main() 