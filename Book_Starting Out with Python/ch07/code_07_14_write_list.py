# code_07_14_write_list.py
# 7.7 Processing lists
## Working with lists and files
### This program saves a list of strings to a file

def main():
    # Create a list of strings.
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas', 'Korea']

    # Open a file for writing
    outfile = open('cities.txt', 'w')

    # Write the list to the file
    for item in cities:
        outfile.write(item + '\n')

    # Close the file
    outfile.close()

# Call the main function
main()