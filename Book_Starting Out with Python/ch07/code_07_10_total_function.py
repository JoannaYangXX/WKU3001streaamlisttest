# code_07_10_total_function.py
# 7.7 Processing lists
## Passing a list as an argument to a function
### This program uses a function to calcuate the total of the values in a list

def main():
    # Create a list.
    numbers = [2,4,6,8,10]

    # Display the total of the list elements
    print('The total is', get_total(numbers))


def get_total(value_list):
    # Create a variable to use as an accumulator
    total = 0

    # Calculate the total of the list elements
    for num in value_list:
        total += num

    # Return the total
    return total

# Call the main function
main()
