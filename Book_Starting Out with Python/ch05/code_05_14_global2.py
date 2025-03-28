# code_05_14_global2.py
#5.6: Global Variables and Global Constants

# Create a global variable
number = 0

def main():
    global number
    number = int(input('Enter a number: '))
    show_number()

def show_number():
    print('The number you entered is', number)

# Call the main function
main()
