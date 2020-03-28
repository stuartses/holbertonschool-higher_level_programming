#!/usr/bin/python3
"""2. Filter states by user input

This module make a MySQL Query using MySQLdb
Filter states with a input name
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
    cur.execute("SELECT * FROM states WHERE BINARY name='{}'"
                " ORDER BY id ASC".format(args[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
