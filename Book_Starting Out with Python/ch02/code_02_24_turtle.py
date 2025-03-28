# code_02_24_turtle.py
import turtle # Start import module
#turtle.setup(640, 480)
turtle.showturtle() # to display the turtle in its window
turtle.write('Hello World')

# Moving turtle forward
turtle.forward(100) # Moving turtle forward

# Turning the turtle
turtle.left(90) # Turn turtle left by 90 degree
turtle.forward(100) # Moving turtle forward
turtle.right(90) # Turn turtle right by 90 degree
turtle.forward(100) # Moving turtle forward

# Setting the turtle's heading
turtle.setheading(90) # set the turtle's heading to a specific angle
turtle.forward(100)
turtle.setheading(180)
turtle.forward(50)
turtle.setheading(270)
turtle.forward(100)

# Pen up or down
turtle.forward(50)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.forward(50)

# Drawing Circles : to draw a circle with a specified radius.
turtle.circle(100) # 100 radius

# Drawing dots
turtle.dot()
turtle.forward(50)
turtle.dot()
turtle.forward(50)
turtle.dot()
turtle.forward(50)


# Changing the pen size and drawing color
turtle.pensize(5)
turtle.pencolor('red')
turtle.circle(100)

# Clear and reset
#turtle.reset()
#turtle.clear()
#turtle.clearscreen()

turtle.reset()

# Moving the turtle to a specific location
turtle.goto(0, 100)
turtle.goto(-100, 0)
turtle.goto(0, 0)

# Filling Shapes
turtle.hideturtle()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()

# Keep the window open. (Not necessary with IDLE.)
turtle.done() 