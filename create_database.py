import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS enquiries(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
phone TEXT,
company TEXT,
service TEXT,
message TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully")