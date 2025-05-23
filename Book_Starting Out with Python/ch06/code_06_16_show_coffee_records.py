# code_06_16_show_coffee_records.py
# 6.3 Processing records
# In the Spotlight: Adding and Displaying Records

# This program displays the records in the coffee.txt file


def main():
    # Open the coffee.txt file
    coffee_file = open('coffee.txt', 'r')

    # Read the first record's description field.
    descr = coffee_file.readline()

    # Read the rest of the file
    while descr != '':
        # Read the quantity field
        qty = float(coffee_file.readline())
        
        # Strip the \n from the description
        descr = descr.rstrip('\n')

        # Display the record
        print('Description: ', descr)
        print('Quantity: ', qty)

        # Read teh next description.
        descr = coffee_file.readline()

    # Close the file
    coffee_file.close()

# Call the main function
main()

