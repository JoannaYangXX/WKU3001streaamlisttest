# code_08_03_login.py
# 8.1 Basic String Operations
## String Slicing
### Extracting Characters from a String

# Background
# At a university, each student is assigned a system login name, which the student uses to log into the campus computer system. As part of your internship with the university’s Informa- tion Technology department, you have been asked to write the code that generates system login names for students. You will use the following algorithm to generate a login name:

    # 1. Get the first three characters of the student’s first name. (If the first name is less than three characters in length, use the entire first name.)
    # 2. Get the first three characters of the student’s last name. (If the last name is less than three characters in length, use the entire last name.)
    # 3. Get the last three characters of the student’s ID number. (If the ID number is less than three characters in length, use the entire ID number.)
    # 4. Concatenate the three sets of characters to generate the login name.

# For example, if a student’s name is Amanda Spencer, and her ID number is ENG6721, her login name would be AmaSpe721. You decide to write a function named get_login_name that accepts a student’s first name, last name, and ID number as arguments, and returns the student’s login name as a string. You will save the function in a module named login.py. This module can then be imported into any Python program that needs to generate a login name. Program 8-3 shows the code for the login.py module.

#### The get_login_name function accepts a first name, last name, and ID number as arguments. It returns a system login name.

def get_login_name(first, last, idnumber):
    # Get the first three letters of the first name. If the name is less than 3 charaters, the slice will return the entire first name.
    set1 = first[0:3]

    # Get the first three letters of the last name. If the name is less than 3 characters, the slice will return the entire ID number.
    set2 = last[0:3]

    # Get the last three charaters of the student ID. If the ID number is less than 3 characters, the slice will return the entire ID number
    set3 = idnumber[-3:]

    # Put the sets of characters together
    login_name = set1 + set2 + set3

    # Return the login name
    return login_name


    