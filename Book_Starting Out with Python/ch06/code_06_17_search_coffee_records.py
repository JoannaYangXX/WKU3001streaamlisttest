# code_06_17_search_coffee_records.py
# 6.3 Processing records
# In the Spotlight: Searching for a Record

# Julie has been using the first two programs that you wrote for her. She now has several records stored in the coffee.txt file and has asked you to write another program that she can use to search for records. She wants to be able to enter a description and see a list of all the records matching that description. Program 6-17 shows the code for the program.

# This program allows the user to search the coffee.txt file for records matching a description

def main():
    # Create a bool variable to use as a flag
    found = False

    # Get the search value
    search = input('Enter a description to search for: ')

    # Open the coffee.txt file
    coffee_file = open('coffee.txt', 'r')

    # Read the first record's description field
    descr = coffee_file.readline()

    # Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        qty = float(coffee_file.readline())

        # Strip the \n from the description
        descr = descr.rstrip('\n')

        # Determine whether this record matches the search value
        if descr == search:
            # Display the record
            print('Description: ', descr)
            print('Quantity: ', qty)
            print()
            # Set the found flag to True
            found = True
        
        # Read the next description
        descr = coffee_file.readline()

    # Close the file
    coffee_file.close()

    # If the search value was not found in the file display a message
    if not found:
        print('That item was not found in the file.')

# Call the main function
main()