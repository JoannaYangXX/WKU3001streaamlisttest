# code_05_29_draw_squares.py
#5.11: Turtle Graphics: Modularizing Code with Functions

# The square function draws a square. The x and y parameters
# are the coordinates of the lower-left corner. The width
# parameter is the width of each side. The color parameter
# is the fill color, as a string.

import turtle

def main():
    turtle.hideturtle()
    square(100, 0, 50, 'red') 
    square(-150, -100, 200, 'blue') 
    square(-200, 150, 75, 'green')
    turtle.done()

def square(x, y, width, color): 
    turtle.penup() 
    turtle.goto(x, y) 
    turtle.fillcolor(color) 
    turtle.pendown() 
    turtle.begin_fill()
    for count in range(4): 
        turtle.forward(width) 
        turtle.left(90)
    turtle.end_fill()

# Raise the pen
# Move to the specified location # Set the fill color
# Lower the pen
# Start filling

main()