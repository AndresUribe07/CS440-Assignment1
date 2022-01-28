from vertex import Vertex


# TODO: Check what to store weights as (float, double)
class Edge:
    def __init__(self, v1: Vertex, v2: Vertex, weight: Vertex):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def __eq__(self, other):
        pass


if __name__ == '__main__':
    from vertex import Vertex

    v1 = Vertex(0, 1)
    v2 = Vertex(1, 1)
    v3 = Vertex(1, 0)
    v4 = Vertex(0, 0)

    e1 = Edge(v1, v2, 11)
    e2 = Edge(v1, v2, 11)
    print(e1 == e2)
