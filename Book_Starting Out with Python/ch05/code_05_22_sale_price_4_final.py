# code_05_22_sale_price_4_final.py
#5.8: Writing Your Own Value-Returning Functions

# This program calculates a retail item's sale price.

# DISCOUNT_PERCENTAGE is used as a global constant for the discount percentage. 
DISCOUNT_PERCENTAGE = 0.20

# The main function. 
def main():
    # Get the item's regular price. Get regular price from user
    regular_price = get_regular_price()
    #print(regular_price)
    # Calculate the sale price.
    sale_price = regular_price - discount(regular_price)
    #print(sale_price)
    # Display the sale price.
    print('The sale price is $', format(sale_price, ',.2f'))

# The get_regular_price function 
def get_regular_price():
    regular_price = float(input("Enter the item's regular price: "))
    return regular_price

# discount function
def discount(price):
    return price * DISCOUNT_PERCENTAGE

# Call the main function.
main()