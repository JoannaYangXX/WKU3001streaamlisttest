# code_07_02_in_linst.py
# 7.4 Finding Items in Lists with the in Operator

# This program demonstrates the in operator used with a list

def main():
    # Create a list of product numbers
    prod_nums = ['V475', 'F987', 'Q143', 'R688']

    # Get a product number to search for.
    search = input('Enter a product number: ')

    # Determine whether the product number is in the list
    if search in prod_nums:
        print(search, 'was found in the list.')
    else:
        print(search, 'was not found in the list.')
    
# Call the main function.
main()


# Program Output (with input shown in bold)
# Enter a product number: Q143 
# Enter Q143 was found in the list.
# Program Output (with input shown in bold)
# Enter a product number: B000 
# Enter B000 was not found in the list.