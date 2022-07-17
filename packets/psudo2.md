# if start, the start probability is start.percent. 
initPriorityQueue(newG, Start, End)
    PriorityQueue = [] # Each Element has deliver_probability, Parent, NodeID. 
    for node in newG
        if node is Start
            PriorityQueue.push([newG[Start].percent, None, Start]) 
        else if node is End
            PriorityQueue.push([0, None, End])
        else 
            PriorityQueue.push([0, None, nodeID])
    return PriorityQueue

# New function, trying to make new problem like old, using directed edges to replicate previous question 
# delivery == not drop probability
modifyG(G)
    newG = []
    # Assume G gives an Edges Nodes and their not drop probability
    for (NodeA, NodeAnotdrop_probability, NodeB, NodeBnotdrop_probability) in G.edges 
        newedge1 = (NodeA, NodeB, NodeAnotdrop_probability)
        newedge2 = (NodeB, NodeA, NodeBnotdrop_probability)
        newG.append(newedge1)
        newG.append(newedge2)

backtrace(Completed, Start, End)
    path = []
    currentNode = Completed[End]
    while currentNode != Start
        path.append(currentNode)
        currentNode = Completed[currentNode].Parent
    return path

packet djikstra 
    # Assume G provides Every (nodeA, nodeB, weight(nodeA, nodeB))
    newG = modifyG(G)
    Completed = []

    PriorityQueue = initPriorityQueue(newG, Start) 

    while PriorityQueue not Empty
        # Assume priority queue pops Node with maximum notdrop_probability
        Node = PriorityQueue.pop()

        if Node.NodeId == End
            Completed.append(Node)
            Break

        # Assume G can provide edges of a node
        for edge in Edges[Node]
            # Assume edge has Node, AdjNode, NodetoAdjNodeProbability
            if PriorityQueue[Node].notdrop_probability * NodetoAdjNodeProbability > PriorityQueue[adjNode].notdrop_probability
                PriorityQueue[adjNode].notdrop_probability = adjNodeNewProbability
                PriorityQueue[adjNode].parent = Node
            
        Completed.append(Node)
    
    return backtrace(Completed, End)