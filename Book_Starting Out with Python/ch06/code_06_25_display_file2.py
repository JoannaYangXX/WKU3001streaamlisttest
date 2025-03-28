# code_06_25_display_file2.py
# 6.4 Exceptions
# This program displays the contents of a file

def main():
    # Get the name of a file
    filename = input('Enter a filename: ')
    try: 
        # Open the file
        infile = open(filename, 'r')
    
        # Read the file's contents.
        contents = infile.read()

        # Display the file's contents.
        print(contents)

        # Close the file
        infile.close()
    except IOError:
        print('An error occurred trying to read')
        print('the file', filename)

# Call teh main function
main()


# Program Output (with input shown in bold)
# Enter a filename: bad_file.txt
# An error occurred trying to read the file bad_file.txt