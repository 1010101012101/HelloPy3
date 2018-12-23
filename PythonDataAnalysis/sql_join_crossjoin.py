import sqlite3

with sqlite3.connect("sql_join_test.db") as con:
    c = con.cursor()
    c.execute("SELECT * FROM employee CROSS JOIN department")