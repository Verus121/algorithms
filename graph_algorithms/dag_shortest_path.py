graph = {
    "r": [("s", 5), ("t", 3)],
    "s": [("t", 2), ("x", 6)],
    "t": [("x", 7), ("y", 4), ("z", 2)],
    "x": [("y", -1), ("z", 1)],
    "y": [("z", -2)],
}

def topological_sort(graph):
    return 0

def main():
    # topological_sort(graph)
    # init_graph

    # for v from topologically sorted graph
        # for from_v_node in Graph.adj[v]
            # relax (v, from_v_node)
    return 0 