import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (1, 'FAITH KARIMI',23,544000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2, 'BOB KURIA',32,400000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3, 'JANE MUTHONI',22,500000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4, 'MARY ANNE',38,300000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5, 'PAUL KAMAU',45,200000.00)")

conn.commit()
print("Records inserted successfully")
conn.close()