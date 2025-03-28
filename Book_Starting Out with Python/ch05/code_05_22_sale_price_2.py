# code_05_22_sale_price_2.py
#5.8: Writing Your Own Value-Returning Functions

# This program calculates a retail item's sale price.


# DISCOUNT_PERCENTAGE is used as a global constant for the discount percentage. 
DISCOUNT_PERCENTAGE = 0.20

# The main function. 
def main():
    # Get the item's regular price. Get regular price from user
    regular_price = get_regular_price()
    print(regular_price)
    # Calculate the sale price.
    sale_price = 0
    # Display the sale price.

# The get_regular_price function 
def get_regular_price():
    regular_price = float(input("Enter the item's regular price: "))
    return regular_price
# discount function

# Call the main function.
main()