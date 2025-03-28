# code_02_15_sale_price.py
# This program gets an item's original price and 
# calculates its sale price, with a 20% discount.

# Get the item's original price.
original_price = float(input("Enter the item's original price: "))

# Calculate the amount of the discount.
discount = original_price * 0.25

# Calculate the sale price.
sale_price = original_price - discount

# Display the sale price.
print('The original price is', original_price, 'Chinese Yuan')
print('The sale price is', sale_price, 'Chinese Yuan')
print('You can save', discount, 'Chinese Yuan')