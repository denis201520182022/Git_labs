import sqlite3

conn = sqlite3.connect("db/database.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS CUSTOMERS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT
)
""")

conn.commit()
conn.close()