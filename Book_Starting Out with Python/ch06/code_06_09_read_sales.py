# code_06_09_read_sales.py
# 6.2 Using loops to process files
# Reading a file with a loop and detecting the end of the file

# This program reads all of the values in the sales.txt file.

def main():
    # Open the sales.txt file for reading.
    sales_file = open('sales.txt', 'r')

    # Read the first line from the file, but don't convert to a number yet. we still need to test for an empty string.
    line = sales_file.readline()

    # As long as an empty string is not naturned from readline, continue processing.
    while line != '':
        # Convert line to a float.
        amount = float(line)

        # Format and display the amount
        print(format(amount, '.2f'))

        # Read the next line
        line = sales_file.readline()
    # close the file
    sales_file.close()

# Call the main function
main()

