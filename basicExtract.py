import sqlite3 as lite
import sys

con = lite.connect('test.db')

with con:
    
    cur = con.cursor()
    cur.execute("SELECT * FROM ARTICLE WHERE AUTHOR LIKE '%Saumya%' AND TITLE LIKE '%Naming%'")
    rows = cur.fetchall()
    print rows

