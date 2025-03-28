# code_06_07_read_numbers.py
# 6.1 Introduction to File Input and Output 터미널 위치를 파이톤 소스 파일로 이동해야 함
# Appending data to an existing file

# This program demonstrates how numbers that are read from a file must be converted from strings before they are used ina math operation

def main():
    # Open a file for reading.
    infile = open('numbers.txt', 'r')

    # Read three numbers from the file
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    # Close the file
    infile.close()

    # Add the three numbers
    total = num1 + num2 + num3

    # Display the numbers and their total
    print('The numbers are:', num1, num2, num3)
    print('Their total is:', total)

# Call the main function
main()

