# -*- coding: utf-8 -*-

import urllib

img = urllib.urlopen('http://data.pr4e.org/cover.jpg')
fhand = open('cover.jpg', 'w')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info)

print size, 'characters copied'
fhand.close()
