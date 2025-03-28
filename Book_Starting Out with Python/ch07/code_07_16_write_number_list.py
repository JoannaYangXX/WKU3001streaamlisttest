# code_07_16_write_number_list.py
# 7.7 Processing lists
## Working with lists and files
### This program saves a list of numbers to a file

def main():
    # Create a list of numbers
    numbers = [1,2,3,4,5,6,7]

    # Open a file for writing.
    outfile = open('numberlist.txt', 'w')

    # Write teh list to the file
    for item in numbers:
        outfile.write(str(item) + '\n')

    # Close the file
    outfile.close()

# Call the main function
main()