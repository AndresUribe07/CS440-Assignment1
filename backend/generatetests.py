import random as rand
import math

COLS = 10
ROWS = 5
PERCENT_BLOCKED = 0.10


def generate_tests(n: int, dirname: str) -> None:
    """
    Given a number of test cases to generate, generates
    n grids with dimensions 100 cols 50 rows 10% of cells randomly blocked
    @param n: number of tests
    @return: generates test cases in a
    """

    for i in range(n):
        cells = generate_vertices_dict(ROWS, COLS)
        # Pick 10% to block
        rand_keys = list(cells.keys())
        rand.shuffle(rand_keys)
        tenpercent = math.floor((COLS * ROWS) * PERCENT_BLOCKED)
        for i in range(tenpercent):
            cells[rand_keys[i]] = 1
        # Randomly pick a start and goal nodes


def generate_vertices_dict(r: int, c: int) -> dict:
    vertices = {}
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            key = str(j) + '|' + str(i)
            vertices[key] = 0

    return vertices

def h(s: tuple, g: tuple):
    return math.sqrt(2) * min(abs(s[0] - g[0]), abs(s[1] - g[1])) + max(abs(s[0] - g[0]), abs(s[1] - g[1])) - min(
        abs(s[0] - g[0]), abs(s[1] - g[1]))


if __name__ == '__main__':
    s = (3, 2)
    g = (0, 0)
    print(h(s, g))
