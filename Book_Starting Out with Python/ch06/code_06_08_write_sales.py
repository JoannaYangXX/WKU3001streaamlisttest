# code_06_08_write_sales.py
# 6.2 Using loops to process files
# Files usually hold large amounts of data, and programs typically use a loop to process the data in a file.

# This program promts the user for sales amounts and writes those amounts to the sales.txt file

def main():
    # Get the number of days.
    num_days = int(input('for how many days do you have sales? '))

    # Open a new file named sales.txt
    sales_file = open('sales.txt', 'w')

    # Get the amount of sales for each day and write it to the file
    for count in range(1, num_days + 1):
        # Get the sales for a day
        sales = float(input('Enter the sales for day #' + str(count) + ': '))
        # Write the sales amount to the file
        sales_file.write(str(sales) + '\n')
    
    # Close teh file
    sales_file.close()
    print('Date written to sales.txt.')

# Call the main function
main()


# Program Output (with input shown in bold)
# For how many days do you have sales? 5 
# Enter Enter the sales for day 
# 1: 1000.0 Enter Enter the sales for day 
# 2: 2000.0 Enter Enter the sales for day 
# 3: 3000.0 Enter Enter the sales for day 
# 4: 4000.0 Enter Enter the sales for day 
# 5: 5000.0 Enter Data written to sales.txt.