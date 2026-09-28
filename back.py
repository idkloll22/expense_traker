import sqlite3
from pathlib import Path

db_name = Path("/app/data/main.db")

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

def fetch_data():
    with sqlite3.connect(db_name) as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM expenses")
        raw_data = cur.fetchall()

        return [dict(row) for row in raw_data]

def delete_data(data_id):
    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM expenses WHERE id = ?", (data_id,))
