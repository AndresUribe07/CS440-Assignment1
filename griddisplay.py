import tkinter
from tkinter import *
from graph import *
from vertex import Vertex
from draw import *


class Display:

    root = Tk()
    root.title = ("Click on vertices for info")
    canvas_name = Canvas(root, width=1000, height=1000) #dimenisons of canvas should be sized better than this
    canvas_name.configure(bg="white")
    canvas_name.pack(fill="x", expand=True)

    def __init__(self, graph):
    #given graph object, sort of does canvas and root on its own
        self.graph = graph

    def coordinate_producer(self):
    #calls methods to draw
        graph = self.graph
        canvas_name = self.canvas_name
        start_vertex = graph.getVertex(graph.start_node_key)
        goal_vertex = graph.getVertex(graph.goal_node_key)

        start_x, start_y = Vertex.getKeyCoordinates(start_vertex)
        start_x *= 100
        start_y *= 100
        goal_x, goal_y = Vertex.getKeyCoordinates(goal_vertex)
        goal_x *= 100
        goal_y *= 100

        points(start_x, start_y, canvas_name, "start", "red", 8) #to indicate the start and goal nodes
        points(goal_x, goal_y, canvas_name, "goal", "red", 8) #this is filled, so it goes before the other filled circles

        for vertex in graph: #goes through vertices

            x, y = Vertex.getKeyCoordinates(vertex)
            x *= 100
            y *= 100
            current_neighbors = vertex.getNeighbors()
            points(x, y, canvas_name, "vertex", "black", 5) #for a graph with vertices and no edges
            
            if len(current_neighbors) != 0: #if there are edges
                for neighbor in current_neighbors:  #goes through a vertex's neighbors
                #PROBLEM: it will re-draw stuff
                    x_neigh, y_neigh = Vertex.getKeyCoordinates(neighbor)
                    x_neigh *= 100
                    y_neigh *= 100
                    points_and_lines(x, y, x_neigh, y_neigh, canvas_name)

        return


    def display_info(self, event):
    #Uses the mouse click location to determine which vertex + print appropriate info
        x = event.x
        y = event.y
        info = ""

        for vertex in self.graph:
            vertex_x, vertex_y = Vertex.getKeyCoordinates(vertex)
            radius = 5 #must be the same as the radius used in the points method under the draw file; that's how big it appears on screen

            if 100*vertex_x in range(x - radius, x + radius) and 100*vertex_y in range(y - radius, y + radius):
            #if clicked coordinates are in the drawn vertex's range
                info = "This vertex's coordinates are " + str(vertex) + ", its g-value is " + str(vertex.g) + ", its h-value is " + str(vertex.h) + ", and its f-value is " + str(vertex.f)
                break
            else: #it's not going to reach this part
                info = "click on vertex, not line or blank space"

        print(info)
        return


    def bind_canvas(self):
    #<Button-1> is for mouse click, "vertex" is the tag of all vertices, display_info is what's run when vertex-tagged object is clicked
        self.canvas_name.tag_bind("vertex", "<Button-1>", self.display_info)
        self.root.mainloop() #displaying the stuff on the canvas