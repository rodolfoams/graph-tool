from io import StringIO

class VertexNotFoundException(Exception):
    def __init__(self,vertex):
        self.vertex = vertex
    def __str__(self):
        return repr(vertex)

class WrongParameterTypeException(Exception):
    def __init__(self,expected,found):
        self.expected = expected
        self.found = found

    def __str__(self):
        return repr("Wrong method parameters type. Expected argument of type <%s> but argument of type <%s> was passed" % (self.expected, self.found))

class Vertex(object):
    def __init__(self, index):
        self.index = index

    def __str__(self):
        with StringIO() as sio:
            sio.write("Vertex%d" % (self.index))
            return sio.getvalue()

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.index == other.index
        return False

    def getIndex(self):
        return self.index

class Edge(object):
    def __init__(self, source, target, weight, index):
        self.source = source
        self.target = target
        self.weight = weight
        self.index = index

    def getSource(self):
        return self.source

    def getTarge(self):
        return self.target

    def getWeight(self):
        return self.weight

    def getIndex(self):
        return self.index

    def __eq__(self, other):
        if isinstance(other, Edge):
            return (self.source == other.source and self.target == other.target) or (self.target == other.source and self.source == other.target)
        return False

class Graph(object):
    def __init__(self,directed=False):
        self.vertices = list()
        self.edges = list()
        self.numVertices = 0
        self.numEdges = 0
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
        newEdge = Edge(source.getIndex(), target.getIndex(),weight,self.numEdges)
        if newEdge in self.edges:
            raise Exception("Edge already exists!")
        pos = 0
        while pos < len(self.edges) and newEdge.weight > self.edges[pos].weight:
            pos += 1
        self.edges.insert(pos,newEdge)
        self.numEdges += 1
        return newEdge

