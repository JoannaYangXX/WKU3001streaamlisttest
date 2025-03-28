# code_05_25_hypothnuse.py
#5.9: The math Module

# This program calculates the length of a right # triangle's hypotenuse.
import math

def main():
    # Get the length of the triangle's two sides.
    a = float(input('Enter the length of side A: ')) 
    b = float(input('Enter the length of side B: '))
    # Calculate the length of the hypotenuse. 
    c = math.hypot(a, b)
    # Display the length of the hypotenuse (삼각형의 빗변 - 하이파티뉴스). 
    print('The length of the hypotenuse is', c)

# Call the main function. 
main()