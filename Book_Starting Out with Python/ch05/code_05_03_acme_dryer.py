# code_05_03_acme_dryer.py
#5.3: Designing a Program to Use Functions

# This program displays step-by-step instructions for disassembling an Acme dryer

# The main function performs the program's main logic.
def main():
    # Display the start-up message.
    startup_message()
    input('Press Enter to see Step 1.')
    step1()
    # Display step 2.
    input('Press Enter to see Step 2.')
    step2()
    # Display step 3.
    input('Press Enter to see Step 3.')
    step3()
    # Display step 4.
    input('Press Enter to see Step 4.')
    step4()

# The startup_message function displays the program's initial message on the screen.
def startup_message():
    print('This program tells you how to')
    print('disassemble an ACME laundry dryer.')
    print('There are four steps in the process.')
    print('')

# For step1
def step1():
    print('Step 1: Unplug the dryer and')
    print('move it away from the wall.')
    print('')
# For step2
def step2():
    print('Step 2: Remove the six screws')
    print('from the back of the dryer.')
    print('')
# For step3
def step3():
    print('Step 3: Remove the back panel')
    print('from the dryer')
    print('')
# For step4
def step4():
    print('Step 4: Pull the top of the')
    print('dryer straight up.')

# Call the main function to begin the program.
main()