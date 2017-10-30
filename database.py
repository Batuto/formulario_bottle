#-*-coding:utf-8-*-
import sqlite3 as lite
import sys

con = lite.connect("data/pipl.db")
print "Creating database/table..."
with con:
    cur = con.cursor()
    #Drop Table
    #cur.execute("DROP TABLE IF EXIST people")

    #Create Tables
    cur.execute("CREATE TABLE people (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, last_name TEXT, bio TEXT, age INTEGER, datetime TEXT)")

con.close()
print "Database/table created."
