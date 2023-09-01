#!/use/bin/python3
"""
a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

mysql_username = argv[1]
mysql_password = argv[2]
database_name = argv[3]
state_name = argv[4]

db_connect = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=mysql_username,
    passwd=mysql_password,
    db=database_name,
)

db_cursor = db_connect.cursor()

db_cursor.execute(
    "SELECT cities.name FROM cities \
        INNER JOIN states ON cities.state_id=states.id \
        WHERE states.name = %s",
    (state_name,),
)
rows_selected = db_cursor.fetchall()

rows_len = len(rows_selected)

for i in range(rows_len):
    if i == rows_len - 1:
        print(rows_selected[i][0], end="")
    else:
        print(rows_selected[i][0], end=", ")
print()