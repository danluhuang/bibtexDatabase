Guide to using this repo:

To build database for the first time: 
1. Open your command shell. 
2. Navigate to a directory where you would like your custom bibtex database to be.
3. As an example, we will name the database as "test.db". Enter the following command into your command shell:
    sqlite3 test.db
    With this line, if a database named "test" is present, it is opened; else, it is created. If you type ls into the command shell now, you can see test.db in this directory. 

To build tables for the first time:
1. Download "basicInsert.py", save it to the directory where your database is. 
2. Open your command shell. Navigate to that directory. 
3. Enter the following command into your command shell: 
	python basicInsert.py
4. In this way, you have created the three tables "ARTICLE", "BOOK", "INPROCEEDINGS" in your test.db

To extract data based on query.txt:
1. Save "query.txt" and "txtExtract.py" to the directory where your database is. 
	Feel free to modify the exact query inside "query.txt", as long as you preserve the format described at the beginning of "txtExtract.py". 
2. Open your command shell. Navigate to that directory. 
3. Enter the following command into your command shell: 
	python txtExtract.py
4. Now you should be able to find a txt file "data.txt" in the same directory containing the result for query.txt 