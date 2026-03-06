import sqlite3

# Database file name
DB_NAME = "students.db"


def connect():
    """
    Create a connection to the SQLite database
    """
    conn = sqlite3.connect(DB_NAME)
    return conn


def create_table():
    """
    Create the students table if it does not exist
    """

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            department TEXT,
            email TEXT
        )
    """)

    conn.commit()
    conn.close()