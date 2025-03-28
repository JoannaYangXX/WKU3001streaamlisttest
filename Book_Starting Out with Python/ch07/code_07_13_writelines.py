# code_07_13_writelines.py
# 7.7 Processing lists
## Working with lists and files
### This program uses the writelines method to save a list of strings to a file

def main():
    # Create a list of strings.
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']

    # Open a file for writing.
    outfile = open('cities.txt', 'w')

    # Write the list to the file
    outfile.writelines(cities)

    # Close the file
    outfile.close()

# Call the main function
main()