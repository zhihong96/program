# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('emaildb.db')
cur = conn.cursor()

cur.execute('drop table if exists Counts')
cur.execute('''
    create table Counts(email TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    #print email
    # 选择 email 不为空
    cur.execute('select count from Counts where email = ?', (email, ))
    row = cur.fetchone() # 得到一条数据
    # 可以作为去重方法，如果无就保存，否则计数加一
    if row is None:
        cur.execute('''insert into Counts(email, count)
            values(?, 1)''', (email, ))
    else:
        cur.execute('update Counts set count = count + 1 where email = ?',
            (email, ))
    conn.commit()

sqlstr = 'select email, count from Counts order by count desc limit 10'
print 'Counts:'
for row in cur.execute(sqlstr):
    print str(row[0]), row[1]

cur.close()
