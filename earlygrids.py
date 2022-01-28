import tkinter as tk

root = tk.Tk()
myCanvas = Canvas(root)
myCanvas.pack()

#square_1, diagonals, and points all create parts of individual grid cells
def square_1(x, y, l, canvasName):
    #draws squares
    x1 = x + l
    y1 = y + l
    return canvasName.create_rectangle(x, y, x1, y1)

def diagonals(x1, y1, x2, y2, canvasName):
    #draws diagonals for each cell
    canvasName.create_line(x1, y1, x2, y2)
    canvasName.create_line(x2, y1, x1, y2)
    return

def points(x, y, canvasName):
    #the points at the corners of the individual graph cells
    #radius is fixed but perhaps could be bigger
    r = 0.5
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)

def graph_cell(x, y, l, canvasName):
    #what makes up one individual graph cell: a square, 4 points, and 2 diagonals
    square_1(x, y, l, canvasName)
    diagonals(x, y, x + l, y + l, canvasName)
    points(x, y, canvasName)
    points(x + l, y, canvasName)
    points(x, y + l, canvasName)
    points(x + l, y + l, canvasName)

def graph_view(x, y, l, rows, columns, canvasName):
    #makes a graph with provided input
    xtemp = x #xtemp and ytemp get changed but original values are still useful
    ytemp = y

    for n in range(0, columns):
        for m in range(0, rows):
            graph_cell(xtemp, ytemp, l, canvasName)
            xtemp += l
        ytemp += l
        xtemp = x

    return


graph_view(5, 5, 30, 2, 4, myCanvas)
#example numbers

root.mainloop()