# code_07_04_index_list.py
# 7.5 List Methods and Useful Built-in Functions

# This program demonstrates how to get the index of an item in a list and then replace that item with a new item

def main():
    # Create a list with some items.
    food = ['Pizza', 'Burgers', 'Chips']

    # Display the list
    print('Here are the items in the food list: ')
    print(food)

    # Get the item to change
    item = input('Which item should I change? ')

    try:
        # Get the item's index in the list
        item_index = food.index(item)

        # Get the value to replace it with
        new_item = input('Enter the new value: ')

        # Replace the old item with the new item.
        food[item_index] = new_item

        # Display the list
        print('Here is the revised list: ')
        print(food)
    except ValueError:
        print('That item was not found in the list.')

# Call the main function
main()



# Program Output (with input shown in bold)
# Here are the items in the food list: 
# ['Pizza', 'Burgers', 'Chips']
# Which item should I change? Burgers 
# Enter the new value: Pickles
# Here is the revised list: 
# ['Pizza', 'Pickles', 'Chips']