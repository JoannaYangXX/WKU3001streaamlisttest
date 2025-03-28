import sqlite3

def main():
    conn = sqlite3.connect('chocolate.db') 
    cur = conn.cursor()
        
    # Get a cursor
    cur = conn.cursor()

    # Add the Products table
    cur.execute('''CREATE TABLE Products (ProductID INTEGER PRIMARY KEY NOT NULL, 
                                          Description TEXT, 
                                          UnitCost REAL,
                                          RetailPrice REAL,
                                          UnitsOnHand INTEGER
                )''')
    
    # Add a row to the Inventory table.
    cur.execute('''INSERT INTO Products (ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
                   VALUES (1, "Dark Chocolate Bar", 2.99, 5.99, 197)''')
    cur.execute('''INSERT INTO Products (ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
                   VALUES (2, "Medium Dark Chocolate Bar", 2.99, 5.99, 406)''')
    cur.execute('''INSERT INTO Products (ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
                   VALUES (3, "Milk Chocolate Bar", 2.99, 5.99, 266)''')
    cur.execute('''INSERT INTO Products (ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
                   VALUES (4, "Chocolate Truffles", 2.99, 11.99, 398)''')
    cur.execute('''INSERT INTO Products (ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
                   VALUES (5, "Chocolate Caramel Bar", 3.99, 6.99, 272)''')
    cur.execute('''INSERT INTO Products (ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
                   VALUES (6, "Chocolate Raspberry Bar", 3.99, 6.99, 363)''')
    cur.execute('''INSERT INTO Products (ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
                   VALUES (7, "Chocolate and Cashew Bar", 4.99, 9.99, 325)''')
    cur.execute('''INSERT INTO Products (ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
                   VALUES (8, "Hot Chocolate Mix", 5.99, 12.99, 222)''')
    cur.execute('''INSERT INTO Products (ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
                   VALUES (9, "Semisweet Chocolate Chips", 1.99, 3.99, 163)''')
    cur.execute('''INSERT INTO Products (ProductID, Description, UnitCost, RetailPrice, UnitsOnHand)
                   VALUES (10, "White Chocolate Chips", 1.99, 3.99, 293)''')
    
    # Commit the change
    conn.commit()

    # Close the connection
    conn.close()

# Excute the main function
if __name__ == '__main__':
    main()
