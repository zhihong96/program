# -*- coding: utf-8 -*-

import sqlite3

conn =sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.execute('drop table if exists Tracks')
cur.execute('create table Tracks (title TEXT, plays INTEGER)')

conn.close()

