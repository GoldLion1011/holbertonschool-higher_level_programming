#!/usr/bin/python3
""" script that takes in the name of a state as an argument
    and lists all cities of that state, using the database hbtn_0e_4_usa """

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT name FROM cities WHERE state_id = (SELECT id\
                FROM states WHERE name=%(target)s)\
                ORDER BY id;", {'target': sys.argv[4]})

    results = cur.fetchall()

    if len(results) <= 0:
        print()
        return

    for i in range(len(results) - 1):
        print(results[i][0], end=", ")
    print(results[len(results) - 1][0])
