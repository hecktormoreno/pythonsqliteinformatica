
import sqlite3

conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM users WHERE name = ?", ("Juan Ponce",))
conn.commit()  # Save the changes
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)
