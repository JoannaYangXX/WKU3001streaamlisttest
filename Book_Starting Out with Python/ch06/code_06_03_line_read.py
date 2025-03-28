# code_06_03_line_read.py
# 6.1 Introduction to File Input and Output 터미널 위치를 파이톤 소스 파일로 이동해야 함
# Reading data from a file

# This program reads the contents of the philosophers.txt file one line at a time.

def main():
    # Open a file named philosophers.txt
    infile = open('philosophers.txt', 'r')

    # Read three line from the file.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # Close the file
    infile.close()

    # Print the data that was read into memory
    print(line3)
    print(line1)
    print(line2)

main()