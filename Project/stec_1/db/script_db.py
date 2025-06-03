import os
import sqlite3

def create_db():
    # Абсолютный путь к базе относительно текущего файла
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "database.db")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT
        )
    ''')
    # Проверим, есть ли уже данные, чтобы не дублировать
    cursor.execute("SELECT COUNT(*) FROM clients")
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute("INSERT INTO clients (name, email, phone) VALUES (?, ?, ?)",
                       ("Иван Иванов", "ivan@example.com", "+70000000001"))
        cursor.execute("INSERT INTO clients (name, email, phone) VALUES (?, ?, ?)",
                       ("Петр Петров", "petr@example.com", "+70000000002"))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
