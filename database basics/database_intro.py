import sqlite3

def create_table() :
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price) :
    conn =  sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()

def view() :
    conn =  sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    print(rows)
    conn.commit()
    conn.close()

def update(item, quantity, price) :
    conn =  sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ? , price = ? WHERE item = ?", (quantity, price, item))
    conn.commit()
    conn.close()

def delete(item) :
    conn =  sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = ? ", (item,))
    conn.commit()
    conn.close()

#create_table()
#insert("Coffee mug", 10, 20)
#insert("water mug", 10, 20)
#insert("Soap", 1, 20)
update('soap box', 20, 4)
view()
delete("soap box")
view()
