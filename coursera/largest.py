# -*- coding: utf-8 -*-

# 最大数
largest = -1
print "Before", largest
number = [9,41,13,3,71,17]
for the_num in number:
    if the_num > largest:
        largest = the_num
    print largest,the_num

print "After", largest

# 求和，计数
count = 0
zork = 0
print "Before", zork
for thing in number:
    count += 1
    zork = zork + thing
    print zork, thing, count
print "After", zork,count

# 最小数
smallest = None
print "Before"
for value in number:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print smallest,value
print "After", smallest

