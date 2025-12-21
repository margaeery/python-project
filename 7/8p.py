from functools import lru_cache
import sqlite3


@lru_cache()
def get_user(user_id):
    print(1)
    conn = sqlite3.connect('8p.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, age FROM users WHERE id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result


conn = sqlite3.connect('8p.db')
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, age INTEGER)"
)
cursor.execute("INSERT INTO users VALUES (1, 'Иван', 25)")
cursor.execute("INSERT INTO users VALUES (2, 'Петя', 25)")
conn.commit()
conn.close()

print(get_user(1))
print(get_user(2))
print(get_user(1))
print(get_user(2))
