# code_05_26_circle_01.py
#5.10: Storing Functions in Modules

# The circle module has functions that perform # calculations related to circles.
import math

def main():
    radius = float(input("Enter the radius: "))
    print('The area of the circle is', format(area(radius), ',.2f')) # 원주의 넓이
    print('The circumference of the circle is', format(circumference(radius), ',.2f')) # 원주의 길이

# The area function accepts a circle's radius as an # argument and returns the area of the circle.
def area(radius):
    return math.pi * radius**2
    # The circumference function accepts a circle's
    # # radius and returns the circle's circumference.

def circumference(radius):
    return 2 * math.pi * radius

main()