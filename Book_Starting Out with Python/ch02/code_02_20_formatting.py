# code_02_20_formatting.py
# An f-string is a special type of string literal that is prefixed with the letter f
print(f'Hello world')

# F-strings support placeholders for variables
name = 'Chad'
print(f'Hello {name}.')

# Placeholders can also be expressions that are evaluated
print(f'The value is {10 + 2}.')

val = 10
print(f'The value is {val + 2}.')

# Format specifiers can be used with placeholders
num = 123.456789
print(f'{num:.3f}')
print(f'{num:.2f}')
print(f'{num:.1f}')
print(f'{num:.0f}')

num = 1000000.00
print(f'{num:,.2f}')

discount = 0.5
print(f'{discount:.0%}')

num = 123456789
print(f'{num:,d}')

num = 12345.6789
print(f'{num:.2e}')

num = 12345.6789
print(f'The number is {num:12,.2f}')

## Alignment
print(f'{num:<20.2f}')
print(f'{num:>20.2f}')
print(f'{num:^20.2f}')

#[alignment][width][,][.precision][type]
print(f'{num:^10,.2f}')

# This program demonstrates how a floating-point
# number can be formatted.
amount_due = 5000.0
monthly_payment = amount_due / 12
print('The monthly payment is',
format(monthly_payment, '.2f'))

