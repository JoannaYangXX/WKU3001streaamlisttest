# You have to write a program to calcualte total commission for salesman.They got 20% of their commission per product until their sales reach to 5000.If the salesaman make more than 5000, they got 50% of commisiion for extra sales .Price for one unit of the product is 600 yuan.


PRODUCT_PRICE = 600  
COMMISSION_RATE_NORMAL = 0.2  
COMMISSION_RATE_EXTRA = 0.5  
SALES_THRESHOLD = 5000  


sales = float(input("Enter the total sales for the salesman (in yuan): "))


if sales <= SALES_THRESHOLD:
    
    commission = sales * COMMISSION_RATE_NORMAL
else:
    
    normal_sales = SALES_THRESHOLD
    extra_sales = sales - normal_sales
    commission = normal_sales * COMMISSION_RATE_NORMAL + extra_sales * COMMISSION_RATE_EXTRA


print(f"The total commission for the salesman is: {commission:.2f} yuan.")