from graph import Graph


def generate_vertices(rows: int, cols: int, g: Graph) -> None:
    """
    Given a number of cell rows and columns, generates the appropriate amount of
    vertices. Note: if there are 4x3 cells there will be 5x4 vertices
    @param rows:
    @param cols:
    @param g:
    @return:
    """
    for i in range(1, rows + 2):
        for j in range(1, cols + 2):
            g.addVertex(str(i) + str(j))


def generate_outer_edges(rows: int, cols: int, g: Graph) -> None:
    """
    Generates outer straight edges does NOT generate inner diagonals
    @param rows:
    @param cols:
    @param g:
    @return: None
    """
    # Generates all horizontal edges
    for i in range(1, rows + 1):
        for j in range(1, cols + 2):
            fromV = str(j) + str(i)
            toV = str(j + 1) + str(i)
            g.addEdge(fromV, toV, 1)
            # print(f'({j},{i}) -- ({j + 1},{i})')

    # Generates all vertical edges
    for x in range(1, rows + 2):
        for y in range(1, cols + 1):
            fromV = str(x) + str(y)
            toV = str(x) + str(y + 1)
            g.addEdge(fromV, toV, 1)
            # print(f'({x},{y}) -- ({x},{y + 1})')

def read_in_graph(filename: str):
    start_node = tuple()
    goal_node = tuple()
    grid_dimensions = tuple()
    g = Graph()

    with open(filename) as f:
        # Read start and goal node coords into a tuple
        line = f.readline().strip()
        tokens = line.split(" ")
        start_node = (int(tokens[0]), int(tokens[1]))

        line = f.readline().strip()
        tokens = line.split(" ")
        goal_node = (int(tokens[0]), int(tokens[1]))

        # Read grid dimensions into a tuple
        line = f.readline().strip()
        tokens = line.split(" ")
        grid_dimensions = (int(tokens[0]), int(tokens[1]))

        generate_vertices(grid_dimensions[0], grid_dimensions[1], g)
        generate_outer_edges(grid_dimensions[0], grid_dimensions[1], g)

    f.close()
    return g


if __name__ == '__main__':
    g = read_in_graph('test.txt')
