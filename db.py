import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully");
conn.execute('drop table if exists students')
conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print("Table created successfully");
conn.close()
