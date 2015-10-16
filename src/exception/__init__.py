class VertexNotFoundException(Exception):
    def __init__(self,vertex):
        self.vertex = vertex
    def __str__(self):
        return repr(self.vertex)

class WrongParameterTypeException(Exception):
    def __init__(self,expected,found):
        self.expected = expected
        self.found = found

    def __str__(self):
        return repr("Wrong method parameters type. Expected argument of type <%s> but argument of type <%s> was passed" % (self.expected, self.found))

