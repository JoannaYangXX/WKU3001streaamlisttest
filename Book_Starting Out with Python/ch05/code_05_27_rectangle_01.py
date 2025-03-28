# code_05_27_rectangle_01.py
#5.10: Storing Functions in Modules

# The rectangle module has functions that perform calculations related to rectangles.

def main():
    width = float(input("Enter the width: "))
    length = float(input("Enter the length: "))
    print('The area of the rectangle is', format(area(width, length), ',.2f')) # 사각형의 넓이
    print('The perimeter of the rectangle is', format(perimeter(width, length), ',.2f')) # 바깥둘래의 길이

# The area function accepts a rectangle's width and length as arguments and returns the rectangle's area.
def area(width, length):
    return width * length

# The perimeter function accepts a rectangle's width and length as arguments and returns the rectangle's perimeter.
def perimeter(width, length):
    return 2 * (width + length)

main()