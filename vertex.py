class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Vertex):
            return self.x == o.x & self.y == o.y


if __name__ == '__main__':
    v1 = Vertex(0, 1)
    v2 = Vertex(1, 1)
    print(v1 == v2)
