import sqlite3

DB_FILE = "assignments.db"

def setup_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()

def store_assignment(filename, content):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO assignments (filename, content) VALUES (?, ?)", (filename, content))
    conn.commit()
    conn.close()

def get_assignments():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assignments")
    assignments = cursor.fetchall()
    conn.close()
    return assignments
