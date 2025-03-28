# code_05_02_two_functions.py
# 5.2: Defining and Calling a Void Function

# This program has two functions. First we define the main function.

# Define the main function.
def main():
    print('I have a message for you.')
    message()
    print('Goodbye!')

# next we define the message function.
def message():
    print('I am Chad,')
    print('A professor of MGS3001')

# Call the main function
main()