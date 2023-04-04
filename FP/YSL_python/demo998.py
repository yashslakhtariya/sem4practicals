import sqlite3 as sq

db = sq.connect('./demo.db')
csr = db.cursor()
csr.execute('create table demo(id int, name text)')
# csr.execute('drop table demo')
db.commit()
