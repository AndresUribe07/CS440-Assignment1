class Vertex:

    def __init__(self, key):  # keys should be strings representing the coordinate Ex: (0,0) is entered as "00"
        self.key = key
        self.neighbors = {}  # vertex: weight

    def addNeighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight

    def getNeighbors(self):
        return self.neighbors.keys()

    def getKey(self):
        return self.key

    def getWeight(self, neighbor):
        return self.neighbors[neighbor]

    # TODO test this
    def __eq__(self, o: object) -> bool:
        return self.key == o.key

    def __str__(self):
        return self.key

    def __repr__(self):
        return self.key

    def __hash__(self):
        return hash(repr(self))

if __name__ == '__main__':
    pass
