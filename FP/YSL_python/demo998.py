import sqlite3 as sq

db = sq.connect('./demo.db')

csr = db.cursor()
# db.execute('create table demotable(id int, name text)')
csr.execute("insert into demotable values (16, 'YSL')")
db.commit()
db.close()