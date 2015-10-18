from io import StringIO
from ..exception import *
from vertex import *
from edge import *

class Graph(object):
    def __init__(self,directed=False):
        self.vertices = list()
        self.edges = list()
        self.numVertices = 0
        self.numEdges = 0
        self.neighbors = dict()
        if not isinstance(directed,bool): raise WrongParameterTypeException("bool", "%s" % (type(directed)))
        self.directed = directed

    def addVertex(self):
        newVertex = Vertex(self.numVertices)
        self.vertices.append(newVertex)
        self.numVertices += 1
        return newVertex

    def addEdge(self, source, target, weight=1):
        v = Vertex(0)
        if (not isinstance(source, type(v))) or (not isinstance(target, type(v))):
            raise WrongParameterTypeException("%s, %s" % (type(v), type(v)), "%s, %s" % (type(source), type(target)))
        if source not in self.vertices:
            raise VertexNotFoundException(source)
        if target not in self.vertices:
            raise VertexNotFoundException(target)
        newEdge = Edge(source, target,weight,self.numEdges)
        if newEdge in self.edges:
            raise Exception("Edge already exists!")
        pos = 0
        while pos < len(self.edges) and newEdge.weight > self.edges[pos].weight:
            pos += 1
        self.edges.insert(pos,newEdge)
        if source not in self.neighbors:
            self.neighbors[source] = list()
        if target not in self.neighbors:
            self.neighbors[target] = list()
        self.neighbors[source].append(newEdge)
        self.neighbors[target].append(newEdge)
        self.numEdges += 1
        return newEdge

