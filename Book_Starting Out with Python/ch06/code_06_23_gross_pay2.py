# code_06_23_gross_pay2.py
# 6.4 Exceptions
# This program calculates gross pay

def main():
    try:
        # Get the number of hours worked
        hours = int(input('How many hours did you work? '))

        # Get the hourly pay rate
        pay_rate = float(input('Enter your hourly pay rate '))

        # Calculate the gross pay
        gross_pay = hours * pay_rate

        # Display the gross pay
        print('Gross pay: $', format(gross_pay, ',.2f'), sep='')
    
    except ValueError:
        print('ERROR: Hours worked and hourly pay rate must be valid numbers.')

# Call the main function
main()
