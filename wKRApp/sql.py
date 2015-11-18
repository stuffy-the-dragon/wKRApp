import sqlite3
import os.path

with sqlite3.connect("db\sample.db") as connection:
	cursor = connection.cursor()
	# cursor.execute("""DROP TABLE posts""")
	cursor.execute("""CREATE TABLE posts(titile TEXT, description TEXT)""")
	cursor.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
	cursor.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')