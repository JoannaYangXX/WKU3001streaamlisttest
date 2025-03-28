# code_05_19_dice.py
#5.7: Introduction to Value-Returning Functions: Generating Random Numbers

# this program the rolling of dice
import random

# Constants for the minimum and maximum random numbers
min = 1
max = 6

def main():
    again = 'y' # create a variable to control the loop

    # simulate rolling the dice
    while again == 'y' or again == 'Y':
        print('Rolling the dice ...')
        print('Their values are: ')
        print(random.randint(min, max))
        print(random.randint(min, max))

        # Do another roll of the dice?
        again = input('Roll them again? (y for Yes): ')

main()