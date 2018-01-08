# -*- coding: utf-8 -*-

import socket
import time

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.imooc.com', 80))
mysock.send('GET https://img1.sycdn.imooc.com/szimg/59eeb21c00012eb205400300.jpg HTTP/1.0\n\n')

count = 0
picture = ""
while True:
    data = mysock.recv(5120)
    if (len(data) < 1): break
    # time.sleep(0.25)
    count = count + len(data)
    print len(data), count
    picture = picture + data

mysock.close()

# Look for the end of the header
pos = picture.find("\r\n\r\n")
print 'Header length', pos
print picture[:pos]

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg", 'wb')
fhand.write(picture)
fhand.close()

