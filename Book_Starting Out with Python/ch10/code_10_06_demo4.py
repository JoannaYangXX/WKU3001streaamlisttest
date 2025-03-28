#code_10_06_demo4.py

# This program imports the coin module and creates an instance of the Coin class

import code_10_05_coin

def main():
    # Create an object from the Coin class
    my_coin = code_10_05_coin.Coin()

    # Display the side of the coin that is facing up
    print('This side is up:', my_coin.get_sideup())

    # Toss the coin
    print('I am going to toss the coin ten times:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

# Call the main function
main()