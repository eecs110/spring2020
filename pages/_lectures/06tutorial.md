---
layout: two-column
title: Practice with Functions
type: tutorial
draft: 1
points: 4
num: 1
notes: Don't forget to sign up for a tutorial slot!
description: Practice creating custom functions
due_date: 2020-04-17
---

<a class="nu-button" href="/spring2020/course-files/tutorials/tutorial01.zip" target="_blank">
    Tutorial Starter Files <i class="fas fa-download"></i>
</a> 

This tutorial is based on content that is reviewed in Lessons 1-4, and is intended to prepare you for [HW2](../assignments/hw2). Please download the starter files and complete the instructions outlined below. PLEASE ASK LOTS OF QUESTIONS in your tutorial section. If you've never done this before, there are a lot of little typing / logic / conceptual mistakes that **everyone** makes (not just you :). Tutorial is your time to allow yourself to make all of those mistakes so that you can learn from them. 

{: .blockquote-no-margin}
> **LEARNING OBJECTIVES:** 
> In order to prepare you for this week's homework, we wanted to use this tutorial session to go over a couple of important logistical and conceptual ideas.
>
> 1. Creating functions
> 2. Working with parameters & arguments
> 3. Making sure that TKinter is successfully running on your machine
> 4. Translating specifications into smaller steps that a computer can solve

## Part 1: Square Challenge
Please open `square_challenge.py` in IDLE, which is located in the `tutorial01` folder. Take a look at it and then run it. You should see something like this:

<img class="small frame" src="/spring2020/assets/images/tutorial01/before1.png" />

### A. Create a make_square function
In this file, write a function called `make_square` that accepts the following arguments:

1. **canvas** *(Canvas)*: a tkinter Canvas object where you want the circle to be drawn.
1. **top_left** *(tuple)*: a tuple -- an point, an (x, y) coordinate -- that defines the top-left position of the square. The first element in the tuple refers to the x-coordinate and the second element in the tuple refers to the y-coordinate.
1. **width (int)**: an int that specifies the width (and also height) of the square.
1. **fill_color (str, optional)**: a string that represents the color of the circle, defaults to a light blue: `#84A9C0`.


### B. Use your make_square function to create a drawing
When you've finished making your `make_square` function, invoke your function to create the pattern pictured below by copying the following code and pasting it ***below*** your function definition, but ***above*** the helpers.make_grid(...) function:

```python
# center blue block
make_square(canvas, (100, 100), 100)

# dark green blocks
make_square(canvas, (0, 0), 100, fill_color='#5B9279')
make_square(canvas, (200, 0), 100, fill_color='#5B9279')
make_square(canvas, (0, 200), 100, fill_color='#5B9279')
make_square(canvas, (200, 200), 100, fill_color='#5B9279')

# light green blocks
make_square(canvas, (50, 200), 50, fill_color='#8FCB9B')
make_square(canvas, (200, 200), 50, fill_color='#8FCB9B')
make_square(canvas, (50, 50), 50, fill_color='#8FCB9B')
make_square(canvas, (200, 50), 50, fill_color='#8FCB9B')
```

<img class="small frame" src="/spring2020/assets/images/tutorial01/after1.png" />

## Part 2: Triangle Challenge
Please open `triangle_challenge.py` in IDLE, which is located in the `tutorial01` folder. Take a look at it and then run it. You should see something like this:

<img class="medium frame" src="/spring2020/assets/images/tutorial01/before2.png" />

### A. Create a make_triangle_left function
TBD


### B. Create a make_triangle_right function
TBD

### C. Use your make_square function to create a drawing
When you've finished making your `make_triangle_left` and `make_triangle_right` functions, invoke these functions to create the pattern pictured below by copying the following code and pasting it ***below*** your function definition, but ***above*** the helpers.make_grid(...) function:

```python
# row 1
make_triangle_right(canvas, (100, 0), 100, fill_color='#5B9279')
make_triangle_left(canvas, (100, 0), 100, fill_color='#5B9279')
make_triangle_right(canvas, (300, 0), 100, fill_color='#5B9279')
make_triangle_left(canvas, (300, 0), 100, fill_color='#5B9279')
make_triangle_right(canvas, (500, 0), 100, fill_color='#5B9279')

# row 2
make_triangle_left(canvas, (0, 100), 100)
make_triangle_right(canvas, (200, 100), 100)
make_triangle_left(canvas, (200, 100), 100)
make_triangle_right(canvas, (400, 100), 100)
make_triangle_left(canvas, (400, 100), 100)

# row 3
make_triangle_right(canvas, (100, 200), 100, fill_color='#8FCB9B')
make_triangle_left(canvas, (100, 200), 100, fill_color='#8FCB9B')
make_triangle_right(canvas, (300, 200), 100, fill_color='#8FCB9B')
make_triangle_left(canvas, (300, 200), 100, fill_color='#8FCB9B')
make_triangle_right(canvas, (500, 200), 100, fill_color='#8FCB9B')
```

<img class="medium frame" src="/spring2020/assets/images/tutorial01/after2.png" />
