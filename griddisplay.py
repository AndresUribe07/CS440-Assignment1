import tkinter
from tkinter import *
from graph import *
from vertex import Vertex
from draw import *


class Display:

    root = Tk()
    root.title = ("Click on vertices for info")
    canvas_name = Canvas(root, width=1000, height=1000) #dimenisons of canvas should be sized better than this, will look @ later
    canvas_name.configure(bg="white")
    canvas_name.pack(fill="x", expand=True)

    def __init__(self, graph):
    #given graph object, sort of does canvas and root on its own
        self.graph = graph

    def coordinate_producer(self):
    #calls methods to draw
        graph = self.graph
        canvas_name = self.canvas_name

        for vertex in graph: #goes through vertices

            x, y = Vertex.getKeyCoordinates(vertex)
            x *= 100 #scale the coordinates up so that they're visible on the canvas
            y *= 100
            current_neighbors = vertex.getNeighbors()

            for neighbor in current_neighbors:  #goes through a vertex's neighbors
            #PROBLEM: it will re-draw stuff
                x_neigh, y_neigh = Vertex.getKeyCoordinates(neighbor)
                x_neigh *= 100
                y_neigh *= 100
                points_and_lines(x, y, x_neigh, y_neigh, canvas_name, vertex)

        return


    def display_info(self, event):
    #Uses the mouse click location to determine which vertex + print appropriate info
        x = event.x
        y = event.y
        info = ""

        for vertex in self.graph:
            vertex_x, vertex_y = Vertex.getKeyCoordinates(vertex)
            vertex_x = vertex_x/100 #the coordinates have been scaled up
            vertex_y = vertex_y/100
            radius = 5 #must be the same as the radius used in the points method under the draw file; that's how big it appears on screen

            if vertex_x in range(x - radius, x + radius) and vertex_y in range(y - radius, y + radius):
            #if clicked coordinates are in the drawn vertex's range
                info = "vertex g: " + str(vertex.g) + " vertex h: " + str(vertex.h)
                break
            else: #it's not going to reach this part
                info = "click on vertex, not line or blank space"

        print(info)
        return


    def bind_canvas(self):
    #<Button-1> is for mouse click, "vertex" is the tag of all vertices, display_info is what's run when vertex-tagged object is clicked
        self.canvas_name.tag_bind("vertex", "<Button-1>", self.display_info)
        self.root.mainloop() #displaying the stuff on the canvas
