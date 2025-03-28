# code_05_06_pass_arg.py
#5.5: Passing Arguments to Functions

# This program demonstrates an argument being passed to a function.

# Define main function
def main():
    value = 5
    show_double(value)

# The show_double function accepts an argument and displays double its value.

# Define show_double
def show_double(number):
    result = number * 2
    print(result)

# Call the main function
main()
