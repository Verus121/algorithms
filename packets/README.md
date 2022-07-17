initPriorityQueue(G, Start, End)
    PriorityQueue = [] # Each Element has deliver_probability, Parent, NodeID. 
    for node in G
        if node is Start
            PriorityQueue.push([1, None, Start]) 
        else if node is End
            PriorityQueue.push([0, None, End])
        else 
            PriorityQueue.push([0, None, nodeID])
    return PriorityQueue
        
backtrace(Completed, Start, End)
    path = []
    currentNode = Completed[End]
    while currentNode != Start
        path.append(currentNode)
        currentNode = Completed[currentNode].Parent
    return path
        
packet_djikstra (G, Start, End)
    # Assume G provides Every (nodeA, nodeB, weight(nodeA, nodeB))
    Completed = []
    PriorityQueue = initPriorityQueue(G, Start) 

    while PriorityQueue not Empty
        # Assume priority queue pops Node with maximum deliver_probability
        Node = PriorityQueue.pop()

        if Node.NodeId == End
            Completed.append(Node)
            Break

        # Assume G can provide edges of a node
        for edge in Edges[Node]
            # Assume edge has Node, AdjNode, NodetoAdjNodeProbability
            if PriorityQueue[Node].deliver_probability * NodetoAdjNodeProbability > PriorityQueue[adjNode].deliver_probability
                PriorityQueue[adjNode].deliver_probability = adjNodeNewProbability
                PriorityQueue[adjNode].parent = Node
            
        Completed.append(Node)
    
    return backtrace(Completed, End)
        