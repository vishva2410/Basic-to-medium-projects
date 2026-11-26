
import sqlite3
def get_connection():
    conn = sqlite3.connect("urls.db")
    conn.row_factory = sqlite3.Row
    return conn
def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_code TEXT UNIQUE NOT NULL,
            original_url TEXT NOT NULL,
            clicks INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    
