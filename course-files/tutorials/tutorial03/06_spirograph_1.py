from tkinter import Canvas, Tk
import random
from helpers import make_circle

gui = Tk()
gui.title('Circle')
# initialize canvas:
canvas = Canvas(gui, width=500, height=500, background='#000022')
canvas.pack()


########################## YOUR CODE BELOW THIS LINE ##############################

# Make the first spirograph pictured
make_circle(canvas, (100, 50), 25)



########################## YOUR CODE ABOVE THIS LINE ############################## 

# makes sure the canvas keeps running:
canvas.mainloop()