# code_08_07_password.py
# this program gets a password from the user and validates it
import code_08_06_login

def main():
    # Get a password from the user.
    password = input('Enter your password: ')

    # Validate the password
    while not code_08_06_login.valid_password(password):
        print('That password is not valid.')
        password = input('Enter your password: ')

    print('That is a valid password.')

#Call the main function
main()