# -*- coding: utf-8 -*-

fhand = open('box.txt','r')
#count = 0
#for line in fhand:
#    count += 1
#print "Line Count:", count

#inp = fhand.read()
#print len(inp)

for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print line

