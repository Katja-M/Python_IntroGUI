import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()
        
    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows

    def search(self, title = "",author = "", year="", isbn=""):
        # Providing a default value for all arguments in case user does not pass any
        self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year =? OR isbn = ?", (title,author, year, isbn))
        rows = self.cur.fetchall()
        self.conn.commit()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id = ?", (id,))
        self.conn.commit()

    def update(self,id, newtitle, newauthor, newyear, newisbn):
        self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (newtitle, newauthor, newyear, newisbn, id))
        self.conn.commit()

    # Since we do not include close() in each method anymore, we
    # need to close the database in the following way
    def __del__(self):
        self.conn.close()
