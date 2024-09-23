import sqlite3

db=sqlite3.connect("contacts.sqlite") # it opens a db if exist or it creates a new db 
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT,phone INTEGER, email TEXT)")
db.execute("Insert into contacts (name, phone,email) VALUES ('Tim',6235324, 'tim@gmail.com')")
db.execute("INSERT INTO contacts (name, phone,email) VALUES('Jon',902914,'jon@gmal.com')")

cursor = db.cursor()
cursor.execute("SELECT  * FROM contacts")
for row in cursor:
    print(row)
cursor.close()

db.close()
