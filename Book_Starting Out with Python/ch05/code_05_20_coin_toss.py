# code_05_20_coin_toss.py
#5.7: Introduction to Value-Returning Functions: Generating Random Numbers

import random

# Constants
head = 1
tails = 2
tosses = 10

def main():
    for toss in range(tosses):
        if random.randint(head, tails) == head:
            print('Heads')
        else:
            print('Tails')

main()