# code_06_27_sales_report2.py
# 6.4 Exceptions
# This program displays the total of the amounts in the sales_data.txt file.
# Sometimes you might want to write a try/except statement that simply catches any exception that is raised in the try suite and, regardless of the exception’s type, responds the same way.

def main():
    # Initialize an accumulator.
    total = 0.0

    try:
        # Open the sales_data.txt file.
        infile = open('sales_data.txt', 'r')

        # Read the values from the file and accumulate them
        for line in infile:
            amount = float(line)
            total += amount

        # Close the file
        infile.close()

        # Print the total.
        print(format(total, ',.2f'))

    except:
        print('An error occurred')

# Call the main function.
main()

# sales_data.txt -> error (An error occurred)
# sales.txt -> 3,300.00