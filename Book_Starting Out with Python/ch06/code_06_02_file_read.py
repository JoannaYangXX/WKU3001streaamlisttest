# code_06_02_file_read.py
# 6.1 Introduction to File Input and Output 터미널 위치를 파이톤 소스 파일로 이동해야 함
# Reading data from a file

# This program reads and displays the contents of the philosophers.txt file

def main():
    # Open a file named philosophers.txt
    infile = open('philosophers.txt', 'r')

    # Read the file's contents
    file_contents = infile.read()

    # Close the file
    infile.close()

    # Print the data that was read into memory
    print(file_contents)

# Call the main function
main()