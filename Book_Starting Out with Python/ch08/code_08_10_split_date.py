# code_08_10_split_date.py
# This program calls the split method, using '/' charater as a separator.

def main():
    # Create a string with a date.
    date_string = '11/26/2018'

    # Split the date.
    date_list = date_string.split('/')

    # display each piece of the date
    print('Month:', date_list[0])
    print('Day:', date_list[1])
    print('Year:', date_list[2])

main()
