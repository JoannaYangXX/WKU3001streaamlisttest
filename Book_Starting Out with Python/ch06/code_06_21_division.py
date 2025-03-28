# code_06_21_division.py
# 6.4 Exceptions

# This program divides a number by another number

def main():
    # Get two numbers
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))

    # If num2 is not 0, divide num1 by num2 and display the result.
    if num2 !=0:
        result = num1/num2
        print(num1, 'divided by', num2, 'is', result)
    else:
        print('Cannot divide by zero')

# Call the main function
main()






# Program Output (with input shown in bold)
# Enter a number: 5
# Enter another number: 2
# 10 divded by 2 is 5.0

# Enter a number: 10 
# Enter another number: 0 
# Cannot divide by zero