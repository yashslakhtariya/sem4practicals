import sqlite3 as sq
from pandas import DataFrame as df
from YSL_io import *

c = sq.connect('prac_11.db')
c.execute('create table if not exists stdnt(id int primary key, name text, contact text, status text)')

s = [
     [64, 'Madhava', '0123456789', 'current'],
     [32, 'Keshava', '1234567890', 'current'],
     [22, 'Govinda', '9876543210', 'alumni'],
     [16, 'Gopinath', '0987654321', 'current'],
     [18, 'Govinda', '9876543210', 'alumni']
]

# Inserting records
for i in s:
     c.execute(f'insert into stdnt values ({str(i[0])}, "{i[1]}", "{i[2]}", "{i[3]}")')
     c.commit()

# Updating a record
c.execute(f'update stdnt set contact = "6432015789" where id = {s[1][0]}')
c.commit()

# Deleting a duplicate record
c.execute(f'delete from stdnt where id = {s[4][0]}')
c.commit()

# Fetching data and printing
data = c.execute('select * from stdnt')

y = df(data, columns=None)

printORNG('\n\tStudents Details : ')
printGRN('\nID   Name    Contact     Status\n')
print(f'{y.to_string(index=False, header=False)}')

c.close()