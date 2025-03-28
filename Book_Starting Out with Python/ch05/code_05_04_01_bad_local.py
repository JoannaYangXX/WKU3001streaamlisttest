# code_05_04_01_bad_local.py
#5.5: Passing Arguments to Functions

# 일부러 에러남 

# Definition of the main function. 
def main():
    get_name()
    print('Hello', name) # This causes an error!

# Definition of the get_name function. 
def get_name():
    name = input('Enter your name: ')

# Call the main function. 
main()