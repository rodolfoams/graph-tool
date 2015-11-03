class Vertex(object):
    def __init__(self, index):
        self.index = index

    def __str__(self):
        return str(self.index)

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.index == other.index
        return False

    def __repr__(self):
        return str(self.index)

    def getIndex(self):
        return self.index

