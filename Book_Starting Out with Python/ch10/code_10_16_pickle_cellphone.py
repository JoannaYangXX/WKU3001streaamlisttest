# code_10_16_pickle_cellphone.py
# This program pickles CallPhone objects.

import pickle
import code_10_12_cellphone

# Constant for the filename
FILENAME = 'cellphones.dat'

def main():
    # Initialize a variable to control the loop.
    again = 'y'

    # Open a file
    output_file = open(FILENAME, 'wb')

    # Get data from the user
    while again.lower() == 'y':
        # Get cell phone data.
        man = input("Enter the manufacturer: ")
        mod = input("Enter the model number: ")
        retail = float(input('Enter the retail price: '))

        # Create a CellPhone object.
        phone = code_10_12_cellphone.CellPhone(man, mod, retail)

        # Pickle the object and write it to the file.
        pickle.dump(phone, output_file)

        # Get more cell phone data?
        again = input("Enter more phone data? (y/n): ")

    # Close the file
    output_file.close()
    print('The data was written to', FILENAME)

main()
