import math
from graph import Graph
import heapq
from vertex import Vertex


def search(g: Graph, updateFunc):
    start_node = g.getVertex(g.start_node_key)
    start_node.g = 0
    start_node.parent = start_node

    goal_node = g.getVertex(g.goal_node_key)

    fringe = []
    start_node.setH(h(start_node, goal_node))
    heapq.heappush(fringe, start_node)
    closed = []
    while len(fringe) > 0:
        s = heapq.heappop(fringe)
        if s == goal_node:
            return "path found"
            # Trace path
        closed.append(s)
        for neighbor in s.getNeighbors():
            succ = g.getVertex(neighbor)
            if not succ in closed:
                if not succ in fringe:
                    succ.g = math.inf
                    succ.parent = None
                updateFunc(s, succ, fringe)
    return "no path found"


def c(s, succ):
    pass


def g(node):
    pass


def h(start_node: Vertex, goal_node: Vertex):
    s = start_node.getKeyCoordinates()
    g = goal_node.getKeyCoordinates()
    return math.sqrt(2) * min(abs(s[0] - g[0]), abs(s[1] - g[1])) + max(abs(s[0] - g[0]), abs(s[1] - g[1])) - min(
        abs(s[0] - g[0]), abs(s[1] - g[1]))


def update_vertex_astar(s, succ, fringe):


def update_vertex_theta(s, succ, fringe):
    pass
