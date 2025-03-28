# code_10_17_unpickle_cellphone.py
# This program unpickles CellPhone objects.

import pickle
import code_10_12_cellphone

# Constant for the filename
FILENAME = 'cellphones.dat'

def main():
    end_of_file = False

    # Open the file
    input_file = open(FILENAME, 'rb')

    # Read to the end of the file
    while not end_of_file:
        try:
            # Unpickle the next object
            phone = pickle.load(input_file)

            # Display the cell phone data
            display_data(phone)
        except EOFError:
            # Set the flag to indicate the end of th efile has been reached.
            end_of_file = True

    # Close the file
    input_file.close()

def display_data(phone):
    print('Manufacturer:', phone.get_manufact())
    print('Model Number:', phone.get_model())
    print('Retail Price: $', 
          format(phone.get_retail_price(), ',.2f'),
          sep = '')
    print()


main()
