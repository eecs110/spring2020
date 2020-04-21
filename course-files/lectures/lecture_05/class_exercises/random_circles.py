'''
Using two built-in python modules, “tkinter” and “random,” create a function
that draws a circle of a random size, position, and color on the screen. 
The function will have a required canvas argument, but any other arguments
should be optional.
Invoke this function many times and see what happens
'''


from tkinter import Canvas, Tk
import random
import time
gui = Tk()
gui.title('Random Circles')

#global variable
canvas = Canvas(gui, width=500, height=500, background='#222222')
canvas.pack()

# how do we generate a random color?

colors = ['#DD6E42', '#E8DAB2', '#4F6D7A', '#C0D6DF', '#EAEAEA']

def generate_hex_color():
    color = '#'
    legal_hex_vals = '0123456789ABCDEF'  #16 characters
    color += random.choice(legal_hex_vals)
    color += random.choice(legal_hex_vals)
    color += random.choice(legal_hex_vals)
    color += random.choice(legal_hex_vals)
    color += random.choice(legal_hex_vals)
    color += random.choice(legal_hex_vals)
    print(color)
    return color


def draw_random_circle():
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    r = random.randint(3, 6)
    top_left = (x - r, y - r)
    bottom_right = (x + r, y + r)
    
    canvas.create_oval([
            top_left,  # top_left
            bottom_right   # bottom_right
        ],  
        fill=colors[random.randint(0, 4)],  # option 1
        # fill=generate_hex_color()
    )

for n in range(0, 2000, 1):
    draw_random_circle()
    time.sleep(.005)
    gui.update()



canvas.mainloop()

