# -*- coding: utf-8 -*-

fhand = open('romeo.txt', 'r')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
         counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    lst.append((val, key))

lst.sort(reverse=True)

for val, key in lst[:10]:
    print key, val

# 简短方法
#c = {...}
#print sorted([(v,k) for k,v in c.items()])

