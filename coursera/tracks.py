# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# make some fresh tables using executescript()
cur.executescript('''
drop table if exists Artist;
drop table if exists Album;
drop table if exists Track;

create table Artist(
    id integer not null primary key autoincrement unique,
    name text unique
);

create table Album(
    id integer not null primary key autoincrement unique,
    artist_id integer,
    title text unique
);

create table Track(
    if integer not null primary key autoincrement unique,
    title text unique,
    album_id integer,
    len integer, rating integer, count integer
);
''')

fname = raw_input('Enter file name: ')
if (len(fname) < 1): fname = 'Library.xml'

def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print 'Dict count:', len(all)
for entry in all:
    if (lookup(entry, 'Track ID') is None):
        continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None:
        continue
    print name, artist, album, count, rating, length

    # ignore: 忽略，如果存在
    cur.execute('''insert or ignore into Artist(name)
        values(?)''', (artist, ))
    cur.execute('select id from Artist where name = ?', (artist, ))
    artist_id = cur.fetchone()[0]

    # 插入或忽略
    cur.execute('''insert or ignore into Album(title, artist_id)
        values(?, ?)''', (album, artist_id))
    cur.execute('select id from Album where title = ?', (album, ))
    album_id = cur.fetchone()[0]

    # 插入或替换/更新
    cur.execute('''insert or replace into Track
        (title, album_id, len, rating, count)
        values (?, ?, ?, ?, ?)''',
        (name, album_id, length, rating, count))
    conn.commit()

