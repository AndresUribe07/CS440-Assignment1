import tkinter as tk
from turtle import goto

root = tk.Tk()
root.configure(background="black")

def create_circle(x,y,r, canvasName):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0,y0,x1,y1)

def create_line(x0, y0, x1, y1, canvasName):
    return canvasName.create_line(x0,y0,x1,y1)

c = tk.Canvas(root, bg="black", height=2500, width=2500)
c.pack()

first_row = 10
first_col = 10
second_row = 50
second_col = 50
third_row = 90
third_col = 90
fourth_col = 130
fifth_col  = 170

#### Creates the 50- eight-neighbor grids
for i in range(1,51):
    # create_circle(col, row, radius, canvas)
    create_circle(first_col, first_row,5,c)
    create_circle(second_col, first_row,5,c)
    create_circle(first_col, second_row,5,c)
    create_circle(second_col, second_row,5,c)
    create_circle(third_col, first_row,5,c)
    create_circle(fourth_col,first_row,5,c)
    create_circle(fifth_col,first_row,5,c)
    create_circle(third_col,second_row,5,c)
    create_circle(fourth_col,second_row,5,c)
    create_circle(fifth_col, second_row,5,c)
    create_circle(first_col, third_row,5,c)
    create_circle(second_col, third_row,5,c)
    create_circle(third_col, third_row,5,c)
    create_circle(fourth_col,third_row,5,c)
    create_circle(fifth_col, third_row,5,c)

    create_line(10,10,10,50,c)
    create_line(10,50,50,50,c)
    create_line(10,10,50,10,c)
    create_line(10,50,50,10,c)
    create_line(50,10,50,50,c)
    create_line(10,10,50,50,c)


    if(i != 0 and i % 5 == 0):
        first_row = 10
        second_row = 50
        third_row = 90
        first_col = first_col + 250
        second_col = second_col + 250
        third_col = third_col + 250
        fourth_col = fourth_col + 250
        fifth_col = fifth_col + 250
    else:
        first_row = first_row + 160
        second_row = second_row + 160
        third_row = third_row + 160

root.mainloop()
