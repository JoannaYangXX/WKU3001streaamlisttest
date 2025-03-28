# code_05_17_random_numbers2.py
#5.7: Introduction to Value-Returning Functions: Generating Random Numbers

# This program displays five random numbers in the range of 1 through 100.
import random

def main():
    for count in range(5):
        number = random.randint(1, 100)
        print(number)

main()