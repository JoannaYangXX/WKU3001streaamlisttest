import sqlite3
def main(): 
    conn = None
    try:
    # Connect to the database and get a cursor. 
        conn = sqlite3.connect('employees.db')
        cur = conn.cursor()
        # Enable foreign key enforcement. 
        cur.execute('PRAGMA foreign_keys=ON')
        # Insert a new row into the Employees table. 
        cur.execute('''INSERT INTO Employees
                            (Name, Position, DepartmentID, LocationID) 
                                   VALUES
                            ("Bill Swift", "Intern", 99, 1)''') 
        print('Employee successfully added.')
    except sqlite3.Error as err:
    # If an exception occurred, print the error message. 
        print(err)
    finally:
    # If the connection is open, then close it. if conn != None:
        conn.close()
# Execute the main function. 

if __name__ == '__main__':
    main()