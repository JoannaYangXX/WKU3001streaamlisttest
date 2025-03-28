import sqlite3

def main():
    conn = sqlite3.connect('employees.db') 
    cur = conn.cursor()
        
    # Get a cursor
    cur = conn.cursor()

    # Add the Products table
    cur.execute('''CREATE TABLE Employees (EmployeeID INTEGER PRIMARY KEY NOT NULL, 
                                          Name TEXT, 
                                          Position TEXT, 
                                          DepartmentID INTEGER,
                                          LocationID INTEGER,
                                          FOREIGN KEY(DepartmentID) REFERENCES Departments(DepartmentID), 
                                          FOREIGN KEY(LocationID) REFERENCES Locations(LocationID)
                )''')
    
    cur.execute('''CREATE TABLE Departments (DepartmentID INTEGER PRIMARY KEY NOT NULL, 
                                          DepartmentName TEXT
                )''')
    
    cur.execute('''CREATE TABLE Locations (LocationID INTEGER PRIMARY KEY NOT NULL, 
                                          City TEXT
                )''')
    
    # Add a row to the Inventory table.
    cur.execute('''INSERT INTO Employees (EmployeeID, Name, Position, DepartmentID, LocationID)
                   VALUES (1, "Arlene Meyers","Director", 4, 4)''')
    cur.execute('''INSERT INTO Employees (EmployeeID, Name, Position, DepartmentID, LocationID)
                   VALUES (2, "Janelle Grant","Engineer", 2, 1)''')
    cur.execute('''INSERT INTO Employees (EmployeeID, Name, Position, DepartmentID, LocationID)
                   VALUES (3, "Jack Smith","Manager", 3, 3)''')
    cur.execute('''INSERT INTO Employees (EmployeeID, Name, Position, DepartmentID, LocationID)
                   VALUES (4, "Sonia Alvarado","Auditor", 1, 2)''')
    cur.execute('''INSERT INTO Employees (EmployeeID, Name, Position, DepartmentID, LocationID)
                   VALUES (5, "Renee Kincaid","Designer", 3, 3)''')
    cur.execute('''INSERT INTO Employees (EmployeeID, Name, Position, DepartmentID, LocationID)
                   VALUES (6, "Curt Green","Supervisor", 2, 1)''')
    cur.execute('''INSERT INTO Departments (DepartmentID, DepartmentName)
                   VALUES (1, "Accounting")''')
    cur.execute('''INSERT INTO Departments (DepartmentID, DepartmentName)
                   VALUES (2, "Manufacturing")''')
    cur.execute('''INSERT INTO Departments (DepartmentID, DepartmentName)
                   VALUES (3, "Marketing")''')
    cur.execute('''INSERT INTO Departments (DepartmentID, DepartmentName)
                   VALUES (4, "Research and Development")''')
    cur.execute('''INSERT INTO Locations (LocationID, City)
                   VALUES (1, "Austin")''')
    cur.execute('''INSERT INTO Locations (LocationID, City)
                   VALUES (2, "Boston")''')
    cur.execute('''INSERT INTO Locations (LocationID, City)
                   VALUES (3, "New York City")''')
    cur.execute('''INSERT INTO Locations (LocationID, City)
                   VALUES (4, "San Jose")''')
    
    # Commit the change
    conn.commit()

    # Close the connection
    conn.close()

# Excute the main function
if __name__ == '__main__':
    main()
