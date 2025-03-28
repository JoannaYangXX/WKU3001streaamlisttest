# code_08_04_generate_login.py
# 8.2 String Slicing
### Extracting Characters from a String

# The get_login_name function accepts three string arguments: a first name, a last name, and an ID number. The statement in line 9 uses a slicing expression to get the first three characters of the string referenced by first and assigns those characters, as a string, to the set1 variable. If the string referenced by first is less than three characters long, then the value 3 will be an invalid ending index. If this is the case, Python will use the length of the string as the ending index, and the slicing expression will return the entire string.
# The statement in line 14 uses a slicing expression to get the first three characters of the string referenced by last, and assigns those characters, as a string, to the set2 variable. The entire string referenced by last will be returned if it is less than three characters.
# The statement in line 19 uses a slicing expression to get the last three characters of the string referenced by idnumber and assigns those characters, as a string, to the set3 variable. If the string referenced by idnumber is less than three characters, then the value −3 will be an invalid starting index. If this is the case, Python will use 0 as the starting index.
# The statement in line 22 assigns the concatenation of set1, set2, and set3 to the login_ name variable. The variable is returned in line 25. Program 8-4 shows a demonstration of the function.

#### This program gets the user's first name, last name, and student ID number. Using this data it generates a system login name.

import code_08_03_login

def main():
    # Get the user's first name, last name, and ID number.
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    idnumber = input('Enter your student ID number: ')

    # Get the login name.
    print('Your system login name is: ')
    print(code_08_03_login.get_login_name(first, last, idnumber))

# Call the main function
main()


# Program Output (with input shown in bold)
# Enter your first name: Jo Enter
# Enter your last name: Cusimano Enter
# Enter your student ID number: BIO4497 
# Enter Your system login name is:
# JoCus497
