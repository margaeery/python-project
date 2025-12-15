import sqlite3

conn = sqlite3.connect('8.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER,"
               " product TEXT)")

cursor.execute("INSERT INTO users VALUES (1, 'Иван')")
cursor.execute("INSERT INTO users VALUES (2, 'Мария')")
cursor.execute("INSERT INTO users VALUES (3, 'Петр')")

cursor.execute("INSERT INTO orders VALUES (1, 1, 'Книга')")
cursor.execute("INSERT INTO orders VALUES (2, 1, 'Ноутбук')")
cursor.execute("INSERT INTO orders VALUES (3, 2, 'Телефон')")

conn.commit()

query = """
SELECT users.name, orders.product
FROM users
JOIN orders ON users.id = orders.user_id
"""

for row in cursor.execute(query):
    print(row)

conn.close()
