class Edge:
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def __eq__(self, other):
        if isinstance(other, Edge):
            return (self.v1 == other.v1) & (self.v2 == other.v2) & (self.weight == other.weight)


if __name__ == '__main__':
    from vertex import Vertex

    v1 = Vertex(0, 1)
    v2 = Vertex(1, 1)
    v3 = Vertex(1, 0)
    v4 = Vertex(0, 0)

    e1 = Edge(v1, v2, 11)
    e2 = Edge(v1, v2, 11)
    print(e1 == e2)
