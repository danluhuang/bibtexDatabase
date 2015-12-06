import sqlite3 as lite
import sys

ARTICLE = (
('bowman:reasoning','Mic Bowman and Saumya K. Debray and Larry L. Peterson', 'Reasoning About Naming Systems', 'ACM Trans. Program. Lang. Syst.',15,5,'795-825','November',1993),
('braams:babel','Johannes Braams','Babel, a Multilingual Style-Option System for Use with LaTeX\'s Standard Document Styles','TUGboat',12,2,'291-301','June',1991),
('herlihy:methodology','Maurice Herlihy','A Methodology for Implementing Highly Concurrent Data Objects','ACM Trans. Program. Lang. Syst.',15,5,'745-770','November',1993)
)

BOOK = (
('Lamport:LaTeX','Leslie Lamport','LaTeX User\'s Guide and Document Reference Manual','Addison-Wesley Publishing Company','Reading, Massachusetts',1986),
('salas:calculus','S.L. Salas and Einar Hille','Calculus: One and Several Variable','John Wiley and Sons','New York',1978)
)

INPROCEEDINGS = (
    ('clark:pct','Malcolm Clark','Post Congress Tristesse','TeX90 Conference Proceedings','84-89','TeX Users Group','March',1991)
)

con = lite.connect('test.db')

with con:
    
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS ARTICLE")
    cur.execute("DROP TABLE IF EXISTS BOOK")
    cur.execute("DROP TABLE IF EXISTS INPROCEEDINGS")

    cur.execute("CREATE TABLE ARTICLE(CITEKEY TEXT, AUTHOR TEXT, TITLE TEXT, JOURNAL TEXT,VOLUME INT, NUMBER INT,PAGES TEXT,MONTH TEXT, YEAR INT)")
    cur.execute("CREATE TABLE BOOK(CITEKEY TEXT, AUTHOR TEXT, TITLE TEXT, PUBLISHER TEXT,ADDRESS INT, YEAR INT)")
    cur.execute("CREATE TABLE INPROCEEDINGS(CITEKEY TEXT, AUTHOR TEXT, TITLE TEXT, BOOKTITLE TEXT,PAGES INT, ORGANIZATION TEXT,MONTH TEXT, YEAR INT)")
    cur.executemany("INSERT INTO ARTICLE VALUES(?,?,?,?,?,?,?,?,?)",ARTICLE)
    cur.executemany("INSERT INTO BOOK VALUES(?,?,?,?,?,?)",BOOK)
    cur.execute("INSERT INTO INPROCEEDINGS VALUES(?,?,?,?,?,?,?,?)",INPROCEEDINGS)
   
    cur.execute("SELECT * FROM ARTICLE")
    rows = cur.fetchall()

    for row in rows:
        print row