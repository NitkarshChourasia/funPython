from tkinter import *

master = Tk()

canva = Canvas(master, width=40, height=60)
canva.pack()

canvas_height = 20
canvas_weight = 200

y = int(canvas_height / 2)
canva.create_line(0, y, canvas_weight, y, fill="#476042")
mainloop()
