# code_06_24_display_file1.py
# 6.4 Exceptions
# This program displays the contents of a file

def main():
    # Get the name of a file
    filename = input('Enter a filename: ')

    # Open the file
    infile = open(filename, 'r')

    # Read the file's contents.
    contents = infile.read()

    # Display the file's contents.
    print(contents)

    # Close the file
    infile.close()

# Call teh main function
main()

# # Program Output (with input shown in bold)
# Enter a filename: coffee.txt
# Brazilian Dark Roast
# 100000.0
# Sumatra Medium Roast
# 25.0

# Program Output (with input shown in bold)
# Enter a filename: bad_file.txt
# Traceback (most recent call last):
# File "C:\Python\display_file.py," line 21, in <module> 
# main()
# File "C:\Python\display_file.py," line 9, in main
# infile = open(filename, 'r')
# IOError: [Errno 2] No such file or directory: 'bad_file.txt'