#code_10_10_account_test2.py
# this program demonstrates the BankAccount class with the __str__method added to it

import code_10_09_bankaccount2 as bankaccount2

def main():
	# Get the starting balance
	start_bal = float(input('Enter your starting balance: '))
	# Create a BankAccount object
	savings = bankaccount2.BankAccount(start_bal)
	# Deposit the user's paycheck
	pay = float(input('How much were you paid this week? '))
	print('I will deposit that into your account.')
	savings.deposit(pay)
	# Display the balance
	print(savings)
	# Get the amount to withdraw
	cash = float(input('How much would you like to withdraw? '))
	print('I will withdraw that from your account.')
	savings.withdraw(cash)
	# Display the balance.
	print(savings)

# Call the main function
main() 