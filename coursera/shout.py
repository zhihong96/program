# -*- coding: utf-8 -*-

#fname = raw_input("Enter a file name: ")
#if len(fname) == 0:
#    fname == 'mbox.txt'
#fhand = open(fname)
fname = 'mbox.txt'
try:
    fhand = open(fname)
except:
    print "error"
    exit()
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    print pieces[1]
