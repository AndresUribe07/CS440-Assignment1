def points(x, y, canvas_name, tag, fill, radius):
#Given coordinates and the canvas name, it draws (and tags) the vertices
    r = radius #radius—can be changed if the circles need to be bigger
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas_name.create_oval(x0, y0, x1, y1, fill=fill, tag=tag)
    #the tag could be changed to be a specific vertex name if needed, probably unnecessary


def lines(x1, y1, x2, y2, canvas_name, fill):
#Given 4 coordinates (for 2 points), draws a line between them. Also passed canvas name and a string for line color
    canvas_name.create_line(x1, y1, x2, y2, fill=fill)
    return


def points_and_lines(x1, y1, x2, y2, canvas_name):
#Given 2 vertices and a canvas name, draws all points and lines between the two vertices
    lines(x1, y1, x2, y2, canvas_name, "black")
    points(x1, y1, canvas_name, "vertex", "black", 5)
    points(x2, y2, canvas_name, "vertex", "black", 5)
    return
