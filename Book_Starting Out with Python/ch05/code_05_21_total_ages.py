# code_05_21_total_ages.py
#5.8: Writing Your Own Value-Returning Functions

# This program uses the return value of a function

def main():
    first_age = int(input('Enter your age: ')) # Get the user's age
    second_age = int(input("Enter your best friend's age:" )) # Get the user's best friend's age
    total = sum(first_age, second_age) # Get the sum(first_age, second_age)
    print('Together your are', total, 'years old.')

# The sum function accepts two numeric arguments and returns the sum of those arguments
def sum(num1, num2):
    result = num1 + num2
    return result

# Call the main function.
main()