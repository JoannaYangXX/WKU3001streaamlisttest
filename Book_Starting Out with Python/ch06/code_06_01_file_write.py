# code_06_01_file_write.py
# 6.1 Introduction to File Input and Output 터미널 위치를 파이톤 소스 파일로 이동해야 함
# Writing data to a file

# This program writes tree lines of data to a file
def main():
    # Open a file named philosophers.txt
    outfile = open('philosophers.txt', 'w')

    # Write the names of three philosphers to the file
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    # Close the file
    outfile.close()

# Call the main function
main()

