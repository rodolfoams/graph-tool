from sys import maxint
from ..core import Edge

def find(vertex, forest):
    for i in xrange(len(forest)):
        if vertex in forest[i]: return i

def closestCityDistance(edges, current, notVisited):
    for e in edges:
        if (e.source == current and e.target in notVisited) or (e.target == current and e.source in notVisited):
            return e.weight
 
def mst(edges, vertices):
    forest = [[v] for v in vertices]
    total = 0
    for edge in edges:
        if edge.target in vertices and edge.source in vertices:
            idxSource = find(edge.source, forest)
            idxTarget = find(edge.target, forest)
            if idxSource != idxTarget:
                forest[idxSource] = forest[idxSource] + forest[idxTarget]
                forest.pop(idxTarget)
                total += edge.weight
        if len(forest) == 1:
            return total

def literalDistance(edges, current, root):
    for e in edges:
        if (e.source == current and e.target == root) or (e.source == root and e.target == current):
            return e.weight

def f(totalDistance, edges, current, root, notVisited):
    if current == root: return totalDistance
    return totalDistance + h(edges, current, root, notVisited)

def h(edges, current, root, notVisited):
    if len(notVisited) == 0:
        return literalDistance(edges, current, root)
    return closestCityDistance(edges, current, notVisited) + mst(edges, notVisited) + closestCityDistance(edges, root, notVisited)

def astarSearch(graph):
    notVisited = list(graph.vertices)
    edges = list(graph.edges)
    edges.sort()
    current = notVisited[0] 
    root = notVisited[0]
    notVisited.remove(current)
    neighbors = dict(graph.neighbors)
    distance = 0
    notVisited.sort()
    while current != root or len(notVisited) > 0:
        if len(notVisited) == 0:
            for e in neighbors[current]:
                if e == Edge(current,root,0,0):
                    distance += e.weight
                    current = root
            continue
        minEstimate = maxint
        nextEdge = None
        for e in neighbors[current]:
            nextNode = None
            if root in e and root != current:
                continue
            if e.source == current:
                if e.target not in notVisited:
                    continue
                nextNode = e.target
            if e.target == current:
                if e.source not in notVisited:
                    continue
                nextNode = e.source
            aux = list(notVisited)
            aux.remove(nextNode)
            d = distance + e.weight
            estimate = f(d,edges,nextNode,root,aux)
            if estimate < minEstimate:
                minEstimate = estimate
                nextEdge = e
        current = (nextEdge.target, nextEdge.source)[nextEdge.target == current]
        distance += nextEdge.weight
        notVisited.remove(current)

    return distance
