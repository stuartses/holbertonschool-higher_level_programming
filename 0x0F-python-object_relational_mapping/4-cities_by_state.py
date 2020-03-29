#!/usr/bin/python3
"""4. Cities by states

This module make a MySQL Query using MySQLdb
Lists all cities
Must enter User, password, host and DB.
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry

"""

if __name__ == "__main__":
    import sys
    import MySQLdb
    len_argv = len(sys.argv) - 1
    args = sys.argv

    db = MySQLdb.connect(host='localhost', user=args[1], passwd=args[2],
                         db=args[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
