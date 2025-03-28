# code_06_14_read_emp_records.py
# 6.3 Processing records

# This program displays the records that are in the employees.txt file.

def main():
    # Open the employees.txt file.
    emp_file = open('employees.txt', 'r')

    # Read the first line from the file, which is the name field of the first record
    name = emp_file.readline()

    # If a field was read, continue processing.
    while name !='':
        # Read the ID number field.
        id_num = emp_file.readline()

        # Read the department field.
        dept = emp_file.readline()

        # Strip the newlines from the field
        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        # Display the record
        print('Name: ', name)
        print('ID: ', id_num)
        print('Dept: ', dept)
        print()

        # Read the name field of the next record.
        name = emp_file.readline()

    # Close the file
    emp_file.close()

# Call the main function
main()

# Program Output
# Name: Ingrid Virgo ID: 4587
# Dept: Engineering

# Name: Julia Rich ID: 4588
# Dept: Research

# Name: Greg Young ID: 4589
# Dept: Marketing