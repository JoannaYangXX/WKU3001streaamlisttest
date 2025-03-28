# code_05_12_keyword_string_args.py
#5.5: Passing Arguments to Functions

# This program demonstrates passing two strings as 
# keyword arguments to a function.
def main():
    first_name = input('Enter your first name: ') 
    last_name = input('Enter your last name: ') 
    print('Your name reversed is') 
    reverse_name(last=last_name, first=first_name)

def reverse_name(first, last): 
    print(last, first)

# Call the main function. 
main()