# code_06_22_gross_pay1.py
# 6.4 Exceptions
# This program calculates gross pay

def main():
    # Get the number of hours worked
    hours = int(input('How many hours did you work? '))

    # Get the hourly pay rate
    pay_rate = float(input('Enter your hourly pay rate '))

    # Calculate the gross pay
    gross_pay = hours * pay_rate

    # Display the gross pay
    print('Gross pay: $', format(gross_pay, ',.2f'), sep='')

# Call the main function
main()

# Program Output (with input shown in bold)
# How many hours did you work? 40
# Enter your hourly pay rate 2
# Gross pay: $80.00

# How many hours did you work? forty
# Traceback (most recent call last):
    # File "C:\Users\Tony\Documents\Python\Source Code\Chapter 06\gross_pay1.py", line 17, in <module>
        # main()
    # File "C:\Users\Tony\Documents\Python\Source
# Code\Chapter 06\gross_pay1.py", line 5, in main
    # hours = int(input('How many hours did you work? '))
# ValueError: invalid literal for int() with base 10: 'forty'