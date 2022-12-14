import sqlite3

#Connect to the database
conn = sqlite3.connect('predictions.db')
c = conn.cursor()

#Create the predictions table
c.execute("""CREATE TABLE predictions (
id INTEGER PRIMARY KEY AUTOINCREMENT,
date DATE,
time TIME,
name TEXT,
morocco INT,
france INT,
extra INT

)""")

conn.commit()
conn.close()