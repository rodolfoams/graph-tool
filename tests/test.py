#!/usr/bin/python

import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from src.core import *
from src.exception import *

def main():
    g = Graph()
    v1 = g.addVertex()
    v2 = g.addVertex()
    v3 = g.addVertex()
    v4 = Vertex(10)

    try:
        e1 = g.addEdge(v1,v2,5)
        print "Created edge from vertex %d to vertex %d with weight %d" % (e1.source.index,e1.target.index,e1.weight)
        e2 = g.addEdge(v1,v3)
        print "Created edge from vertex %d to vertex %d with weight %d" % (e2.source.index,e2.target.index,e2.weight)
        e3 = g.addEdge(v2,v1,1)
        print "Created edge from vertex %d to vertex %d with weight %d" % (e3.source.index,e3.target.index,e3.weight)

    except Exception as e:
        print e

    finally:
        try:
            e4 = g.addEdge(v1,v4)
            print "Created edge from vertex %d to vertex %d with weight %d" % (e4.source.index,e4.target.index,e4.weight)
        except VertexNotFoundException as e:
            print "Vertex %d not found! " % e.vertex.index


if __name__ == "__main__":
    main()
