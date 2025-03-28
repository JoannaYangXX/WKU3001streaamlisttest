# code_05_16_random_numbers1.py
#5.7: Introduction to Value-Returning Functions: Generating Random Numbers

# This program displays a random number in the range of 1 through 10
import random

def main():
    number = random.randint(1, 10) # Get a random number
    print('The number is', number) # Display the number

# Call the main function.
main()
