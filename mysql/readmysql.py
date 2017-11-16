# -*- coding: utf-8 -*-

import pymysql.cursors

connection=pymysql.connect(host='localhost',
            port=3306,
            user='root',
            passwd='****',
            db='testdata',
            charset='utf8')

try:
    cur=connection.cursor()
    sql="select urlname,urlhref from urls"
    conut=cur.execute(sql)
    print conut
    result=cur.fetchall()
    print result
finally:
    connection.close()
