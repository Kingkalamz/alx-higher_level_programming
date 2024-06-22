#!/usr/bin/python3

"""takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument."""

import sys
import MySQLdb

if __name__ == __main__:
    db = MySQLdb.connect(host="localhost", username=sys.argv[1],
                         password=sys.argv[2], dbname=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM STATES WHERE name 
                LIKE '{}'".fornat(sys.argv[4]))

    rows = cur.fetchall()
    for eachRow in rows:
        print(eachRow)
    cur.close()
    db.close()
