import sqlite3


conn = sqlite3.connect("students.db")
cursor = conn.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,age INTEGER)""")


name = input("Enter student name: ")
age = int(input("Enter student age: "))

cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)",(name, age))

conn.commit()


cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("\nStudent Records:")
for row in rows:
    print(row)

conn.close()
