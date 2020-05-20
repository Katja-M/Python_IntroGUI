import sqlite3

# Standard process
# 1. Connect to a database
# 2. Create a cursor object
# 3. Write an SQL query
# 4. Commit change to a database
# 5. Close database connection

def create_table():
    # Create a connection which is stored in a variable
    # Passing a database file as argument
    # If you do not have a database file yet, this line of codes creates the database
    conn = sqlite3.connect('mystore.db')

    # Create a cursor object
    cursor = conn.cursor()
    # Pointing to cursor object for SQL code
    cursor.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = sqlite3.connect('mystore.db')
    # Create a cursor object
    cursor = conn.cursor()
    # Adding data to database
    cursor.execute("INSERT INTO store VALUES (?,?,?)", (item,quantity, price))
    conn.commit()
    conn.close()

insert("Coffee Cup", 10, 5.5)

def view():
    conn = sqlite3.connect('mystore.db')
    cur =conn.cursor()
    cur.execute("SELECT * FROM store")
    # Fetching data
    rows = cur.fetchall()
    conn.close()
    return rows

print(view())

def delete(item):
    conn = sqlite3.connect('mystore.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM store WHERE item = ?', (item,))
    conn.commit()
    conn.close()

delete("Coffee Cup")
print(view())

def update(quantity, price, item):
    conn = sqlite3.connect('mystore.db')
    cur = conn.cursor()
    cur.execute('UPDATE store SET quantity = ?, price = ? WHERE item = ?', (quantity, price, item))
    conn.commit()
    conn.close()

update(11,6,'Coffe Cup')
print(view())