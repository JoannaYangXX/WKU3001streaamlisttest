# code_04_20_turtle_octagon.py
# Drawing rect
import turtle
for x in range(4): 
    turtle.forward(100) 
    turtle.right(90)

# Move turtle
turtle.penup()
turtle.goto(200, 0)
turtle.pendown()

# Drawing Octagon
for x in range(8): 
    turtle.forward(100) 
    turtle.right(45)


# Turtle done
turtle.done()