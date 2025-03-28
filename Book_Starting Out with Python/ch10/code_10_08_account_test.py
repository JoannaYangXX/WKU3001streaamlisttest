#code_10_08_account_test.py
# This program demonstrates the BankAccount class
import code_10_07_bankaccount as bankaccount

def main():
    # Get the starting balance
    start_bal = float(input('Enter your starting balance: '))

    # Create a BankAccount object
    savings = bankaccount.BankAccount(start_bal)

    # deposit the user's paycheck
    pay = float(input('How much were you paid this week? '))
    print('I will deposit that into your account.')
    savings.deposit(pay)

    # Display the balance
    print('Your account balance is $',
    format(savings.get_balance(), ',.2f'),
    sep='')

    # Get the amount to withdraw
    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your account.')
    savings.withdraw(cash)

    # Display the balance
    print('Your account balance is &',
    format(savings.get_balance(), ',.2f'),
    sep='')

# Call the main function
main()
