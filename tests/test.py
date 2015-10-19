#!/usr/bin/python

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src import *

def main():
    g = Graph()
    g2 = loadTSPLIBDataset("brazil58")
    print "Criado um grafo com %d vertices e %d arestas" % (g2.numVertices, g2.numEdges)
#    print "Blind...", blindSearch(g2)
#    print "Greedy...", greedySearch(g2)
#    print "A*...", astarSearch(g2)
    print "Genetic...", geneticSearch(g2)
    v1 = g.addVertex()
    v2 = g.addVertex()
    v3 = g.addVertex()
    v4 = Vertex(10)

    try:
        e1 = g.addEdge(v1,v2,5)
        e2 = g.addEdge(v1,v3)
        e3 = g.addEdge(v2,v1,1)

    except Exception as e:
        pass

    finally:
        try:
            e4 = g.addEdge(v1,v4)
        except VertexNotFoundException as e:
            pass

if __name__ == "__main__":
    main()
