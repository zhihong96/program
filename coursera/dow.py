# -*- coding: utf-8 -*-

fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    words = line.split()
    #if line == '': continue
    #print words
    if len(words)<1: continue
    if words[0] != "From": continue
    print '------', words[2]
