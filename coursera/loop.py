# -*- coding: utf-8 -*-

while True:
    line = raw_input(">")
    if line[0] == '#':
        continue
    if line == "done":
        break
    print line
print "Done"
