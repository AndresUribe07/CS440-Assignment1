import tkinter as tk

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

c = tk.Canvas(root, bg="black", height=200, width=200)
c.pack()

create_circle(10,10,5,c)
create_circle(50,10,5,c)
create_circle(10,50,5,c)
create_circle(50,50,5,c)
create_circle(90,10,5,c)
create_circle(130,10,5,c)
create_circle(170,10,5,c)
create_circle(90,50,5,c)
create_circle(130,50,5,c)
create_circle(170,50,5,c)
create_circle(10,90,5,c)
create_circle(50,90,5,c)
create_circle(90,90,5,c)
create_circle(130,90,5,c)
create_circle(170,90,5,c)





create_line(10,10,10,50,c)
create_line(10,50,50,50,c)
create_line(10,10,50,10,c)
create_line(10,50,50,10,c)
create_line(50,10,50,50,c)
create_line(10,10,50,50,c)


root.mainloop()
