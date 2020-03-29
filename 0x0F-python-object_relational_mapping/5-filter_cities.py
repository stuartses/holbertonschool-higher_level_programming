#!/usr/bin/python3
"""5. All cities by state

This module make a MySQL Query using MySQLdb
Takes in the name of a state as an argument and lists all cities of that state
Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry

"""

if __name__ == "__main__":
    import sys
    import MySQLdb
    args = sys.argv

    db = MySQLdb.connect(host='localhost', user=args[1], passwd=args[2],
                         db=args[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE BINARY states.name=%s "
                "ORDER BY cities.id ASC", (args[4],))

    rows = cur.fetchall()
    print(", ".join([str(row[0]) for row in rows]))

    cur.close()
    db.close()
