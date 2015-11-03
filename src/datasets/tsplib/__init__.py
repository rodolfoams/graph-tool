import sys
from .. import *
from os.path import join, dirname 

def loadTSPLIBDataset(dataset):
    path = join(dirname(__file__),dataset) + ".tsp"
    with open(path,"r") as f:
        content = f.readlines()
    lineCounter = 1
    while "EDGE_WEIGHT_SECTION" not in content[lineCounter-1]: lineCounter += 1
    edgeSets = content[lineCounter:-1]
    g = Graph()
    numVertices = len(edgeSets) + 1
    for i in xrange(numVertices):
        g.addVertex()
    for i in xrange(len(edgeSets)):
        edgeSet = map(int, edgeSets[i].strip().split(" "))
        pEdge = 0
        for j in xrange(i+1,numVertices):
            g.addEdge(g.vertices[i],g.vertices[j],edgeSet[pEdge])
            pEdge += 1
    g.populateNeighbors()
    return g
        
