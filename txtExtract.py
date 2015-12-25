# created by Danlu Huang, Zhengning Han
# This python script is used for extracting user input query from a txt file named "query.txt" and extracting relevant data from the database "ARTICLE"
# The odd number lines in "query.txt" should be keywords of the database/of a bibtex file, e.g. AUTHOR, TITLE, DATE, etc. 
# The even number lines in "query.txt" should be user-provided information corresponding to the keyword one the line above. 
# It can consist of multiple words as long as they are on the same line. 


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
    output = open("result.txt","w")
    output.write(str(rows))
    output.close()

