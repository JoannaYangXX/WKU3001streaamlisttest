# circle.py
#5.10: Storing Functions in Modules

# The circle module has functions that perform # calculations related to circles.
import math

# The area function accepts a circle's radius as an # argument and returns the area of the circle.
def area(radius):
    return math.pi * radius**2
    # The circumference function accepts a circle's
    # # radius and returns the circle's circumference.

def circumference(radius):
    return 2 * math.pi * radius
