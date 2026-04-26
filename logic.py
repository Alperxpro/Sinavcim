import sqlite3

def init_db():
    con=sqlite3.connect("sınavcım.db")
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS dersler(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ders TEXT)""")
    con.commit()
    con.close()

def add_data(ders):
    con=sqlite3.connect("sınavcım.db")
    cur=con.cursor()
    cur.execute("INSERT INTO dersler(ders)VALUES (?)",(ders,))
    con.commit()
    con.close()

def select_data():
    con=sqlite3.connect("sınavcım.db")
    cur=con.cursor()
    cur.execute("SELECT ders FROM dersler")
    data=cur.fetchall()
    con.close()
    return data

if __name__ == "__main__":
    init_db()




