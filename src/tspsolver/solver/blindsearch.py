from random import shuffle

def blindSearch(graph):
    notVisited = list(graph.vertices)
    edges = list(graph.edges)
    shuffle(notVisited)
    shuffle(edges)
    totalCost = 0
    root = notVisited[0]
    current = notVisited[0]
    notVisited.remove(current)
    neighbors = dict(graph.neighbors)
    for e in edges:
        if len(notVisited) == 0: break
        modified = False
        if current == e.source and e.target in notVisited:
            totalCost += e.weight
            current = e.target
            modified = True
        if current == e.target and e.source in notVisited:
            totalCost += e.weight
            current = e.source
            modified = True
        if modified: notVisited.remove(current)

    for e in neighbors[current]:
        if root == e.target or root == e.source:
            totalCost += e.weight

    return totalCost
