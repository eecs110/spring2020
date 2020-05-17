---
layout: two-column
title: Error Handling
type: tutorial
draft: 0
points: 4
num: 5
description:
  - Practicing with try/except
due_date: 2020-05-23
    
---

<style>
    .bash-small .highlighter-rouge {
        width: 520px;
        margin: auto;
        margin-top: 10px;
    }
</style>

<a class="nu-button" href="/spring2020/course-files/tutorials/tutorial05.zip" target="_blank">
    Tutorial Starter Files <i class="fas fa-download"></i>
</a> 


## Background
In preparation for Tic Tac Toe, we are going to help you get started by helping you to handle runtime errors. As you may recall, runtime errors typically happen when your program encounters data that was not adequately anticipated by the programmer. Examples of runtime errors include encountering (a) data with the wrong data type (e.g. a string instead of an int), or (b) data that doesn't make sense for the given context.

### Error Handling in HW5
In [Homework 5](../assignments/hw5), you will be creating a Tic-Tac-Toe game where a user will play a computer in a game of Tic-Tac-Toe. One critical part of engineering the game is making sure that your user enters the right input. Specifically:

{:.bash-small}
1. The user must enter an integer between 1-9.
2. The user cannot enter a number corresponding to a slot that has already been taken. For instance, in the scenario below, if the user (represented by the symbol `o`) types the number `5`, the program should refuse the request and explain to the user why their move is illegal (because the 5-slot is already take by `x`).
```bash
               |   |                7 | 8 | 9 
            ———————————            ———————————
             x | x |                4 | 5 | 6 
            ———————————            ——————————— 
               | o |                1 | 2 | 3 
```

## Your Task
Please make the following enhancements to the `tictactoe_starter.py` file (which correspond to the ability for the user to play their move):
1. If the user does not enter a number from 1-9, tell them their entry was invalid and that they should try again (use try/except as well as if/else).
2. If the user enters a valid number that is not empty, tell them that slot is already taken.
3. If the user types "Q", terminate the program.
4. Keep re-prompting the user until they enter a valid number (or Q). See sample video:

## What to turn in (same deal as always)
As described in the syllabus, there are two ways to earn full participation credit in each tutorial session:

1. By attending them (synchronously), working through the exercises, and asking questions (as they arise).
2. By turning in the tutorial exercise(s) ON CANVAS **before** the tutorial session.

Whichever option you choose, you will be expected to know the material reviewed in the tutorial for the exam, and are encouraged to fully complete and submit the tutorial assignments (though this is not required if you attended the tutorial).
