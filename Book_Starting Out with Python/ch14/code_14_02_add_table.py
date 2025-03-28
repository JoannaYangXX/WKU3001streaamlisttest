import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('inventory.db')
    
    # Get a cursor
    cur = conn.cursor()

    # Add the Inventory table
    cur.execute('''CREATE TABLE Inventory (ItemID INTEGER PRIMARY KEY NOT NULL, ItemName TEXT, Price REAL)''')

    # Commit the change
    conn.commit()

    # Close the connection
    conn.close()

# Excute the main function
if __name__ == '__main__':
    main()
