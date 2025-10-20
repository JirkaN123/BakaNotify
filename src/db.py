import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        class_name TEXT DEFAULT '3O',
        notifications_enabled INTEGER DEFAULT 1
    )""")
    conn.commit()
    conn.close()

def get_user(user_id):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT class_name, notifications_enabled FROM users WHERE user_id = ?", (user_id,))
    result = c.fetchone()
    conn.close()
    return result

def set_user(user_id, class_name):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO users (user_id, class_name, notifications_enabled) VALUES (?, ?, 1)",
              (user_id, class_name))
    conn.commit()
    conn.close()
