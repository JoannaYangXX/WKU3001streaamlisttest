# code_07_08_total_list.py
# 7.7 Processing lists
## Totalling the values in a list
### This program calculates the total of the value in a list

def main():
    # Create a list.
    number = [2,4,6,8,10]

    # Create a variable to use as an accumulator
    total = 0

    # Calculate the total of the list elements
    for value in number:
        total += value

    # Display the total of the list elements
    print('The total of the elements is', total)

# Call the main function
main()