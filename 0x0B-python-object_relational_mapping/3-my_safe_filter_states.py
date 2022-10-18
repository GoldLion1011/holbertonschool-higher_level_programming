#!/usr/bin/python3
""" Script that takes in arguments and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument
    AND is also safe from MySQL injections """

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    state = sys.argv[4
    ]
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY\
                %(name)s ORDER BY states.id", {'name : state'})
    rows = cur.fetchall()

    if rows is None:
        return False

    for row in rows:
        print(row)

    cur.close()
    db.close()
