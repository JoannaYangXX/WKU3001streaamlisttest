# This program calculates sales commissions
# Calculating a series of commission
While keep_going =='y'
# Get a salesperson's sales and commission rate 
sales = float (input("Enter the amount of sales:"))
comm_rate = float(input("Enter the commision rate:"))
# Calculate the commission(sales*commission rate)
commission = sales * comm_rate
# Display the commssion
print (f"Your commission is ${commission:,.2f}")
keep_going = input("Do you want to calculate another
                   commission(Enter y for yes):")