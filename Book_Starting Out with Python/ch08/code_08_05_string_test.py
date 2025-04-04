# code_08_05_string_test.py
# 8.3 Testing, searching, and manipulating strings
## String Testing Methods
### This program demonstrates several string testing methods

def main():
    # Get a string from the user.
    user_string = input('Enter a string: ')

    print('This is what I found about that string: ')

    # Test the string
    if user_string.isalnum():
        print('The string is alphanumeric.')
    if user_string.isdigit():
        print('The string contains only digits.')
    if user_string.isalpha():
        print('The string contains only alphabetic charaters.')
    if user_string.isspace():
        print('The string contains only whitespace charaters.')
    if user_string.islower():
        print('The letters in the string are all lowercase.')
    if user_string.isupper():
        print('The letters in the string are all uppercase')

# Call the string
main()
    
