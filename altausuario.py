
import sqlite3

conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
''')

cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Rambo lee", "johndoe1@example.com"))
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Juan Ponce", "johndoe1@example.com"))
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Juan Ponce", "johndoe1@example.com"))
conn.commit()  # Save the changes to the database

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
