def blindSearch(graph):
    notVisited = list(graph.vertices)
    edges = list(graph.edges)
    totalCost = 0
    root = notVisited[0]
    current = notVisited[0]
    notVisited.remove(current)
    while len(notVisited) > 0:
        for e in edges:
            if current == e.source and e.target in notVisited:
                totalCost += e.weight
                current = e.target
                break
            if current == e.target and e.source in notVisited:
                totalCost += e.weight
                current = e.source
                break
        notVisited.remove(current)

    for e in edges:
        if (current == e.source and root == e.target) or (current == e.target and root == e.source):
            totalCost += e.weight

    return totalCost
