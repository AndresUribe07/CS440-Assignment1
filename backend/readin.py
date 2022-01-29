from graph import Graph


def generate_vertices(rows: int, cols: int, g: Graph) -> list:
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

        # Generate vertices
        new_vertices = generate_vertices(grid_dimensions[0], grid_dimensions[1], g)

        # TODO Find a way to generate outside edges programmatically
        
        # TODO Any benefit in representing vertices as a matrix instead of a list?

    f.close()
    return g


if __name__ == '__main__':
    g = read_in_graph('test.txt')
    print(g.vertices)
