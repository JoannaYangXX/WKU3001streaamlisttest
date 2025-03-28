# code_05_04_02_bad_local_fix.py
#5.4: Local Variables

# 일부러 에러남 

# Definition of the main function. and pass value to print_name
def main():
    name = input('Enter your name: ')
    print_name(name)

# Define print_name    
def print_name(name_from_main):
    print('Hello', name_from_main)

# Call the main function. 
main()