
import sqlite3

conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()
cursor.execute("UPDATE users SET email = ? WHERE name = ?", ("test1@example.com", "Rambo lee"))
conn.commit()  # Save the changes

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
