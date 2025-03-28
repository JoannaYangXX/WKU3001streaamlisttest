# code_04_22_spiral_circles.py
# This program draws a design using repeated circles.
import turtle

# Named constants
NUM_CIRCLES = 36
RADIUS = 100
ANGLE = 10
ANIMATION_SPEED = 0

# Number of circles to draw # Radius of each circle
# Angle to turn
# Animation speed
# Set the animation
turtle.speed(ANIMATION_SPEED)

# Draw 36 circles, with the turtle tilted
# by 10 degrees after each circle is drawn.
for x in range(NUM_CIRCLES):
    turtle.circle(RADIUS)
    turtle.left(ANGLE)

turtle.done()