#!/usr/bin/python3
"""3. SQL Injection

This module make a MySQL Query using MySQLdb
Avoid MySQL injection
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry

"""

if __name__ == "__main__":
    import sys
    import MySQLdb
    len_args = len(sys.argv) - 1
    args = sys.argv

    db = MySQLdb.connect(host='localhost', user=args[1], passwd=args[2],
                         db=args[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name=%s"
                " ORDER BY id ASC", (args[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
