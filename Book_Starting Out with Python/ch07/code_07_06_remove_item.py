# code_07_06_remove_item.py
# 7.5 List Methods and Useful Built-in Functions

# This program demonstrates how to use the remove method to remove an item from a list

def main():
    # Create a list with some items.
    food = ['Pizza', 'Burgers', 'Chips']

    # Display the list
    print('Here are the items in the food list:')
    print(food)

    # Get the item to change
    item = input('Which item should I remove? ')

    try:
        # Remove the item
        food.remove(item)

        # Display the list
        print('Here is the revised list:')
        print(food)
    except ValueError:
        print('That item was not found in the list')

# Call the main function
main()