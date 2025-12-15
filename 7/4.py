import sqlite3

conn = sqlite3.connect('4.db')
cursor = conn.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS users "
    "(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
)

users = [
    (1, 'Иван', 25),
    (2, 'Мария', 30),
    (3, 'Алексей', 35)
]

cursor.executemany("INSERT INTO users VALUES (?, ?, ?)", users)

conn.commit()

for row in cursor.execute("SELECT * FROM users"):
    print(row)

cursor.execute("UPDATE users SET age = 26 WHERE id = 1")
cursor.execute("UPDATE users SET age = age + 1")

conn.commit()

print()
for row in cursor.execute("SELECT * FROM users"):
    print(row)

conn.close()
