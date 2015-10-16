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

