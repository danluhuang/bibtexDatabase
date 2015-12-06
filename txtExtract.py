import sqlite3 as lite
import sys

con = lite.connect('test.db')

def extractKeywords(filename):
	inputQuery = "SELECT * FROM ARTICLE WHERE "

	with open(filename,'r') as f:
		lineNumber = 1 #odd for keywords, even for user spedified queries
		for line in f: 
			if lineNumber==1:
				inputQuery = inputQuery +line.rstrip('\r\n') + " LIKE "
			elif lineNumber%2==1:
				inputQuery = inputQuery + " AND "+line.rstrip('\r\n') + " LIKE "
			else: 
				inputQuery = inputQuery + "'%" + line.rstrip('\r\n') + "%'"
			lineNumber+=1

	return inputQuery


with con:
    
    # to preven the printed string from having a prefix "u" which indicates unicode, 
    # use this line to change the defualt type to string
    con.text_factory = str

    cur = con.cursor()
    inputQuery = extractKeywords("query.txt")
    cur.execute(inputQuery)
    rows = cur.fetchall()
    print str(rows)

