# code_06_05_strip_newline.py
# 6.1 Introduction to File Input and Output 터미널 위치를 파이톤 소스 파일로 이동해야 함
# Reading a String and Stripping the Newline from It

# This program reads the contents of the philosophers.txt file on line at a time.

def main():
    # Open a file named philosophers.txt
    infile = open('philosophers.txt', 'r')

    # Read three lines from the file
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # Strip the \n in from each string
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')

    # Close the file
    infile.close()

    # Print the data that was read into memory
    print(line1)
    print(line2)
    print(line3)

# Call the main function
main()


