# code_05_24_square_root.py
#5.9: The math Module

import math

def main():
    # Get a number
    number = float(input('Enter a number: '))

    # Get the square root of the number
    square_root = math.sqrt(number)

    # Display the square root
    print('The square root of', number, '0 is', square_root)

main()