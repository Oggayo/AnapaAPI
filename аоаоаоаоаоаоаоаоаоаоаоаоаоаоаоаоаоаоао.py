import sqlite3 as sql

with sql.connect('Abema') as con:
    cur = con.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS products
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
        name TEXT,
        number INTEGER
        unit TEXT DEFAULT("шт.")
        price REAL DEFAULT (0.0)
""")
con.commit()