# This program will calculate payment in normal case ,you will get 1,000 yuan per hour.legal work hour per week is 40. Your contract said ,if you work more than legal work than legal work hour ,you will get different pay ratio,overtime pay radio,1.5.You will write a program that get input from worker and calulate the total payment considering normal hour or overtime work hour

# GLobal Variables
BASE_HOUR = 40
HOURLYOAYMENT = 1000
OT_PAYRATIO = 1.5
# Get working hours from employee
workhour = int(input("Enter your working hours for this week:"))
# Determine whether working hour is >= 40
# If workhour <= 40
if workhour <=40:
    #Total payment
    Total_payment = workhour * HOURLYPAYMENT
    # Display total payment
    print{f"You work{workhour} this week, so your total payment of this week is {total_payment}"}
# Otherwise
else
    # Calculate total payment with overtime payment
    withforth_payment = BASE_HOUR * HOURLYPAYMENT
    overtime = workhour -BASE_HOUR
    overtime_payment = overtime * HOURLYPAYMENT * OT_PAYRATIO
    total_payment = withforth_payment +overtime_payment 
    # Display total payment
    print(f"You worked {workhour} hours this week, including {overtime} overtime hours.")
    print(f"Your base payment is {base_payment} yuan.")
    print(f"Your overtime payment is {overtime_payment} yuan (overtime ratio: {OT_PAYRATIO}x).")
    print(f"Your total payment is {total_payment} yuan.")
 



