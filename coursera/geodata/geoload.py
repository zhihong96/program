# -*- coding: utf-8 -*-

import urllib
import sqlite3
import json
import time
import ssl

# Google API (requires API key)
# serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"
# If you are in China this URL might work (with key):
# serviceurl = "http://maps.google.cn/maps/api/geocode/json?"

serviceurl = "http://python-data.dr-chuck.net/geojson?"

# Deal with SSL cretificate anomalies Python > 2.7
# scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
scontext = None

conn =sqlite3.connect('geodat.sqlite')
cur = conn.cursor()

cur.execute('''
    create table if not exists Locations (address text, geodata text)''')

fh = open("where.data")
count = 0
for line in fh:
    if count > 200:
        print 'Retrieved 200 locations, restart to retrieve more'
        break
    address = line.strip()
    print ''
    cur.execute("select geodata from Locations where address= ?",
        (buffer(address), ))

    try:
        data = cur.fetchone()[0]
        print "Found in database", address
        continue
    except:
        pass

    print 'Resolving', address
    url = serviceurl + urllib.urlencode({"sensor":"false",
        "address": address})
    print 'Retrieving', url
    uh = urllib.urlopen(url, context=scontext)
    data = uh.read()
    print 'Retrieves', len(data), 'characters', data[:20].replace('\n',' ')
    count = count + 1
    try:
        js = json.loads(str(data))
        #print js # We print in case unicode causes an error
    except:
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
        print '=== Failure To Retriece ==='
        print data
        continue

    cur.execute('''insert into Locations (address, geodata)
        values(?, ?)''', (buffer(address), buffer(data)))
    conn.commit()
    if count % 10 == 0:
        print 'Pausing for a bit...'
        time.sleep(3)
