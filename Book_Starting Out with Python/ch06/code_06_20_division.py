# code_06_20_division.py
# 6.4 Exceptions

# This program divides a number by another number

def main():
    # Get two numbers
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))

    # Divide num1 by num2 and display the result.
    result = num1/num2
    print(num1, 'divded by', num2, 'is', result)

# Call the main function
main()


# Program Output (with input shown in bold)
# Enter a number: 5
# Enter another number: 2
# 10 divded by 2 is 5.0

# Enter a number: 10 
# Enter another number: 0 
# Traceback (most recent call last):
    # File "C:\Python\division.py," line 13, in <module>
# main()
    # File "C:\Python\division.py," line 9, in main
# result = num1 / num2
# ZeroDivisionError: integer division or modulo by zero
