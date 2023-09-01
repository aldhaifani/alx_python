#!/use/bin/python3
"""
a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
And safe from SQL INJETCIONs
"""
import MySQLdb
from sys import argv

mysql_username = argv[1]
mysql_password = argv[2]
database_name = argv[3]
state_name_searched = argv[4]


db_connect = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=mysql_username,
    passwd=mysql_password,
    db=database_name,
)

db_cursor = db_connect.cursor()

db_cursor.execute("SELECT * FROM states WHERE name=%s", (state_name_searched,))
rows_selected = db_cursor.fetchall()

for row in rows_selected:
    print(row)
