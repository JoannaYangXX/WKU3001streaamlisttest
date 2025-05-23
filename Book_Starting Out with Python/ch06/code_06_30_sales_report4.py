# code_06_30_sales_report4.py
# 6.4 Exceptions
# This program displays the total of the amounts in teh sales_data.txt file

def main():
    # Initialize an accumulator
    total = 0.0

    try:
        # Open the sales_data.txt file
        infile = open('sales_data.txt', 'r')

        # Read the values from the file and accumulate them
        for line in infile:
            amount = float(line)
            total += amount

        # Close the file
        infile.close()
    except Exception as err:
        print(err)
    else:
        # Print the total.
        print(format(total, ',.2f'))

# Call the main function
main()

