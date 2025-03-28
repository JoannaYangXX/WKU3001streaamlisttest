# code_05_11_keyword_args.py
#5.5: Passing Arguments to Functions

# 이 예제는 키워드 아규먼트를 시연함

def main():
    # Show the amount of simple interest, using 0.01 as
    # interest rate per period, 10 as the number of periods,
    # and $10,000 as the principal.
    show_interest(rate = 0.01, periods = 10, principal = 10000.0)

# The show_interest function displays the amount of simple interest for a given principal,
# interest rate, per period, and number of periods

def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print('The simple interest will be $',
    format(interest, ',.2f'),
    sep = "")

# Call the main function
main()