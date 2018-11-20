'''
Check PGAdmin to view database
'''


import psycopg2

def create_table() :
    conn = psycopg2.connect("dbname='database1' user='postgres' password ='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price) :
    conn =  psycopg2.connect("dbname='database1' user='postgres' password ='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item, quantity, price))
    conn.commit()
    conn.close()

def view() :
    conn =  psycopg2.connect("dbname='database1' user='postgres' password ='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    print(rows)
    conn.commit()
    conn.close()

def update(item, quantity, price) :
    conn =  psycopg2.connect("dbname='database1' user='postgres' password ='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s , price = %s WHERE item = %s", (quantity, price, item))
    conn.commit()
    conn.close()

def delete(item) :
    conn =  psycopg2.connect("dbname='database1' user='postgres' password ='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s ", (item,))
    conn.commit()
    conn.close()

create_table()
#insert("soap box", 10, 20)
#insert("orange", 20, 30)
#insert("water mug", 10, 20)
#insert("Soap", 1, 20)
#update('soap box', 20, 4)
view()
#delete("soap box")
