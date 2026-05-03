import sqlite3

def init_db():
    con=sqlite3.connect("sınavcım.db")
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS ortaokul(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ders TEXT)""")
    con.commit()
    con.close()

def add_data(ders):
    con=sqlite3.connect("sınavcım.db")
    cur=con.cursor()
    cur.execute("INSERT INTO ortaokul(ders)VALUES (?)",(ders,))
    con.commit()
    con.close()

def select_data():
    con=sqlite3.connect("sınavcım.db")
    cur=con.cursor()
    cur.execute("SELECT ders FROM ortaokul")
    data=cur.fetchall()
    con.close()
    return data

if __name__ == "__main__":
    init_db()




