import sqlite3
import os

# delete the database if it exists
os.remove('club.db')

#  connect to db
connection = sqlite3.connect('club.db')

# create cursor
cursor = connection.cursor()

# create table
cursor.execute("CREATE TABLE members (firstname, lastname, email)")

# verify table creation
rows = cursor.execute("SELECT * FROM sqlite_master").fetchall()
print(rows)

#write data to table
cursor.execute('''INSERT INTO members VALUES
    ('peter','parker','peter@mit.edu),
    ('bruce','wayne','bruce@mit.edu')
    ('tony','stark','tony@mit.edu')
''')

#commit changes
connection.commit()

rows = cursor.execute("SELECT * FROM members").fetchall()
print(rows)

connection.close