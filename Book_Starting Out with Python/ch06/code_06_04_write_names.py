# code_06_04_write_names.py
# 6.1 Introduction to File Input and Output 터미널 위치를 파이톤 소스 파일로 이동해야 함
# Concatenating a newline to a string

# This program gets three names from the user and writes them to a file

def main():
    # Get three names.
    print('Enter the names of three friends.')
    name1 = input('Friend #1: ')
    name2 = input('Friend #2: ')
    name3 = input('Friend #3: ')

    # Open a file named friends.txt
    myfile = open('friends.txt', 'w')

    # Write the name to the file.
    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')

    # Close the file
    myfile.close()
    print('The names were written to friends.txt.')

# Call the main function
main()