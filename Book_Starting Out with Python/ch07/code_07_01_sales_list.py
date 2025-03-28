# code_07_01_sales_list.py
# 7.2 Introduction to Lists

# The NUM_DAYS constant holds the number of days that we will gether sales data for
NUM_DAYS = 5

def main():
    # Create a list to hold the sales for each day
    sales = [0] * NUM_DAYS

    # Create a variable to hold an index
    index = 0

    print('Enter the sales for each day.')

    # Get the sales for each day.
    while index < NUM_DAYS:
        print('Day #', index + 1, ': ', sep='', end='')
        sales[index] = float(input())
        index += 1

    # Display the values entered
    print('Here are the values you entered: ')
    for value in sales:
        print(value)

# Call the main function.
main()


# Output
# Enter the sales for each day.
# Day #1: 100
# Day #2: 150
# Day #3: 170
# Day #4: 120
# Day #5: 140
# Here are the values you entered: 
# 100.0
# 150.0
# 170.0
# 120.0
# 140.0