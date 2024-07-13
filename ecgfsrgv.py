import sqlite3 as sq


db = sq.connect('users')
sql = db.cursor()

sql.execute(''' CREATE TABLE IF NOT EXISTS users(login TEXT, password TEXT) ''')

db.close()
