def greedySearch(graph):
    notVisited = list(graph.vertices)
    edges = list(graph.edges)
    edges.sort()
    totalCost = 0
    e0 = edges[0]
    totalCost += e0.weight
    semiVisited = list()
    semiVisited.append(e0.source)
    semiVisited.append(e0.target)
    notVisited.remove(e0.source)
    notVisited.remove(e0.target)
    edges.remove(e0)
    while len(notVisited) > 0 or len(semiVisited) > 0:
        for e in edges:
            if len(notVisited) == 0 and e.source in semiVisited and e.target in semiVisited:
                totalCost += e.weight
                semiVisited.remove(e.source)
                semiVisited.remove(e.target)
                edges.remove(e)
                break

            if e.source in notVisited and e.target in semiVisited:
                totalCost += e.weight
                notVisited.remove(e.source)
                semiVisited.append(e.source)
                semiVisited.remove(e.target)
                edges.remove(e)
                break

            if e.source in semiVisited and e.target in notVisited:
                totalCost += e.weight
                notVisited.remove(e.target)
                semiVisited.append(e.target)
                semiVisited.remove(e.source)
                edges.remove(e)
                break

    return totalCost
    
