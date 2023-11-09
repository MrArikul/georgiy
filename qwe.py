from tkinter import Tk, Canvas, CENTER
from grid import Grid
from human import Human

root= Tk()
canvas = Canvas(root,width=800,height=600)
canvas.pack()

grid = Grid(canvas)
grid.display()

p1 = Human(canvas, 300, 600)
p1.display()



root.mainloop()