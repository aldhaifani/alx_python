#!/use/bin/python3
"""
a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

mysql_username = argv[1]
mysql_password = argv[2]
database_name = argv[3]

db_connect = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=mysql_username,
    passwd=mysql_password,
    db=database_name,
)

db_cursor = db_connect.cursor()

db_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
rows_selected = db_cursor.fetchall()

for row in rows_selected:
    print(row)
