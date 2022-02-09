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
    #points(x1, y1, canvas_name, "vertex", "black", 7)
    points(x2, y2, canvas_name, "vertex", "black", 7)
    return


def split_coordinates(string):
#same as the method "getKeyCoordinates" in the Vertex class. however, that works with vertices, this is for when A*/theta* pass list of strings (coordinates)
    x_coord = ""
    y_coord = ""
    is_x = True
    char_coords = [char for char in string]

    for c in char_coords:
        if c == '|':
            is_x = False
            #y_coord += c
        elif is_x:
            x_coord += c
        else:
            y_coord += c

    coord_list = [int(x_coord), int(y_coord)]
    return coord_list


def draw_path(path_list, canvas_name, fill):
#can be called on list of coordinates that A* or Theta* return. Pass it the list, a Display object's canvas, and preferred fill color
    for coordinate in range(0, len(path_list) - 1):
        x1, y1 = split_coordinates(path_list[coordinate])
        x2, y2 = split_coordinates(path_list[coordinate + 1])
        x1 *= 50
        y1 *= 50
        x2 *= 50
        y2 *= 50
        lines(x1, y1, x2, y2, canvas_name, fill)
