class Vertex:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, o: object) -> bool:
        pass


if __name__ == '__main__':
    v1 = Vertex(0, 1)
    v2 = Vertex(1, 1)
    print(v1 == v2)