import sqlite3

def connect():
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    con.commit()
    cur.close()

def insert(title, author, year, isbn):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("INSERT INTO books VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))
    con.commit()
    cur.close()

def view():
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    con.close()
    return rows

def search(title="", author="", year="", isbn=""):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    con.close()
    return rows

def delete(id=""):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (id, ))
    con.commit()
    con.close()

def update(id, title, author, year, isbn):
    con=sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    con.commit()
    con.close()

connect()
#insert("The Earth", "John Smith", 1923, 76873894)
#print(search(title="The sea"))
#delete(2)
#update(1, "The moon", "John Smooth", 1917, 99999)
print(view())