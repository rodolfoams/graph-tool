from io import StringIO
from ..exception import *
from vertex import *
from edge import *
from sys import maxint

class Graph(object):
    def __init__(self,directed=False):
        self.vertices = list()
        self.edges = list()
        self.numVertices = 0
        self.numEdges = 0
        self.neighbors = None
        self.sparseMatrix = None
        if not isinstance(directed,bool): raise WrongParameterTypeException("bool", "%s" % (type(directed)))
        self.directed = directed

    def addVertex(self):
        newVertex = Vertex(self.numVertices)
        self.vertices.append(newVertex)
        self.numVertices += 1
        self.updateSparseMatrix()
        return newVertex

    def initializeSparseMatrix(self):
        self.sparseMatrix = list()
        aux = [maxint] * self.numVertices
        for i in xrange(self.numVertices):
            self.sparseMatrix.append(list(aux))

    def updateSparseMatrix(self):
        if self.sparseMatrix == None:
            self.initializeSparseMatrix()
        if self.numVertices > len(self.sparseMatrix):
            for l in self.sparseMatrix:
                l.append(maxint)
            self.sparseMatrix.append([maxint]*self.numVertices)

    def populateNeighbors(self):
        self.neighbors = dict()
        for e in self.edges:
            if e.source not in self.neighbors:
                self.neighbors[e.source] = list()
            if e.target not in self.neighbors:
                self.neighbors[e.target] = list()
            self.neighbors[e.source].append(e)
            self.neighbors[e.target].append(e)

    def addEdge(self, source, target, weight=1):
        newEdge = Edge(source, target,weight,self.numEdges)
        self.edges.append(newEdge)
        self.sparseMatrix[source.index][target.index] = min(weight,self.sparseMatrix[source.index][target.index])
        self.sparseMatrix[target.index][source.index] = min(weight,self.sparseMatrix[target.index][source.index])
        self.numEdges += 1
        return newEdge

