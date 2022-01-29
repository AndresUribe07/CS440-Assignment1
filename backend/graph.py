from vertex import Vertex
from edge import Edge


class Graph:
    def __init__(self, vertices: list, edges: list):
        self.vertices = vertices
        self.edges = edges

    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, x: int, y: int) -> None:
        """
        Given the x and y value of a vertex add it to the graph
        @param x:
        @param y:
        @return:
        """
        pass

    def add_vertices(self, vertices_list: list):
        """
        Given a list of vertices, append all vertices to the self.vertices list
        @param vertices_list:
        @return: None
        """
        self.vertices.extend(vertices_list)

    # TODO check if edges need to be saved as doubles and how to get a double in python
    def add_edge(self, v1: Vertex, v2: Vertex, weight) -> None:
        """
        Given two vertices and an edge weight add an edge to a graph
        @param v1:
        @param v2:
        @param weight:
        @return:
        """
        pass
