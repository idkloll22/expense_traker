import sqlite3

db_name = "main.db"

with sqlite3.connect(db_name) as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date INTEGER NOT NULL,
        description TEXT NOT NULL,
        amount INTEGER NOT NULL
    ) """)

def add_expenses(date, description, amount):
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        cur.execute("INSERT INTO expenses (date, description, amount) VALUES(?, ?, ?)",
            (date, description, amount)
        )
        print("s")
