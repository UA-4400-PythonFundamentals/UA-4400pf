# linguist/db.py

import sqlite3

_conn: sqlite3.Connection | None = None

def get_connection() -> sqlite3.Connection:
    global _conn
    if _conn is None:
        _conn = sqlite3.connect(":memory:")
        _conn.row_factory = sqlite3.Row
    return _conn

def init_db() -> None:
    conn = get_connection()
    c = conn.cursor()
    # тимчасово виключаємо FK, щоб без помилок дропнути попередні
    c.execute("PRAGMA foreign_keys = OFF;")
    c.execute("DROP TABLE IF EXISTS card;")
    c.execute("DROP TABLE IF EXISTS deck;")
    c.execute("DROP TABLE IF EXISTS user;")
    c.execute("PRAGMA foreign_keys = ON;")

    c.execute("""
    CREATE TABLE user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    );
    """)
    c.execute("""
    CREATE TABLE deck (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY(user_id) REFERENCES user(id) ON DELETE CASCADE
    );
    """)
    c.execute("""
    CREATE TABLE card (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        word TEXT NOT NULL,
        translation TEXT NOT NULL,
        tip TEXT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES user(id) ON DELETE CASCADE
    );
    """)
    conn.commit()

def reset_db() -> None:
    global _conn
    if _conn is not None:
        _conn.close()
    _conn = None
    init_db()

init_db()