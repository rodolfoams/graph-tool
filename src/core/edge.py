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

