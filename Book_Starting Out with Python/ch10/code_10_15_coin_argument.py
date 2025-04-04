# code_10_15_coin_argument.py
# This program passes a coin object as an argument to a function
import code_10_05_coin as coin

# main function
def main():
	# Create a Coin object
	my_coin = coin.Coin()
	# This will display 'Heads'
	print(my_coin.get_sideup())
	# Pass the object to the flip function
	flip(my_coin)
	# This might display 'Heads', or it might display 'Tails'
	print(my_coin.get_sideup())

def flip(coin_obj):
	coin_obj.toss()

# Call the main function
main()