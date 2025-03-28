# code_06_28_gross_pay3.py
# 6.4 Exceptions
# This program calculates gross pay.

def main():
    try:
        # Get the number of hours worked.
        hours = int(input('How many hours did you work? '))

        # Get the hourly pay rate
        pay_rate = float(input('Enter your hourly pay rateL: '))

        # Calculate the gross pay
        gross_pay = hours * pay_rate

        # Display the gross pay
        print('Gross pay: $', format(gross_pay, ',.2f'), sep='')
    
    except ValueError as err:
        print(err)

# Call the main function
main()

# How many hours did you work? 40
# Enter your hourly pay rateL: 2
# $80.00

# How many hours did you work? forty
# invalid literal for int() with base 10: 'forty