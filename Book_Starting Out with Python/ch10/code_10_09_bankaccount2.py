# code_10_09_bankaccount2.py
# The BankAccount class simulates a bank account
class BankAccount:
	
	# The __init__ method accepts an argument for the account's balance. It si assigned to the __balance attribute
	def __init__(self, bal):
		self.__balance = bal
	
	# the deposit method makes a deposit into the account
	def deposit(self, amount):
		self.__balance += amount

	# The withdraw method withraws an amount from the account
	def withdraw(self, amount):
		if self.__balance >= amount:
			self.__balance -= amount
		else:
			print('Error: Insufficient funds')

	# The get_balance method returns the account balance
	def get_balance(self):
		return self.__balance

	# The __str__ method returns a string indicating the object's state
	def __str__(self):
		return 'The balance is $' + format(self.__balance, ',.2f')
		