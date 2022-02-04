def points(x, y, canvas_name, vertex_name):
#Given coordinates and the canvas name, it draws (and tags) the vertices
    r = 5 #radius—can be changed if the circles need to be bigger
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas_name.create_oval(x0, y0, x1, y1, fill="black", tag="vertex")
    #the tag could be changed to be a specific vertex name if needed, probably unnecessary


def lines(x1, y1, x2, y2, canvas_name, fill):
#Given 4 coordinates (for 2 points), draws a line between them. Also passed canvas name and a string for line color
    canvas_name.create_line(x1, y1, x2, y2, fill=fill)
    return


def circle(x, y, canvas_name): #for indicating if a vertex is a start or goal node
    r = 8
    x0 = x -r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas_name.create_oval(x0, y0, x1, y1, fill="red")


def points_and_lines(x1, y1, x2, y2, canvas_name, vertex_name):
#Given 2 vertices and a canvas name, draws all points and lines between the two vertices
    lines(x1, y1, x2, y2, canvas_name, "black")
    points(x1, y1, canvas_name, vertex_name)
    points(x2, y2, canvas_name, vertex_name)
    return
