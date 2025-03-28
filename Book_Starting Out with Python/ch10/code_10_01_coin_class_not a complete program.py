#code_10_01_coin_class_not a complete program.py
import random

# The coin class simulates a coin that can be flipped

class Coin:
    # The __init__ method initializes the sideup data attribute with 'Heads'
    def __init__(self):
        self.sideup = 'Heads'
    
    # The toss method generates a random number in the range of 0 throught 1. If the number is 0, then sideup is set to 'Head'. Otherwise, sideup is set to 'Tails'.
    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    # The get_sideup method returns the value referenced by sideup
    def get_sideup(self):
        return self.sideup