# -*- coding: utf-8 -*-

# 求平均数
count = 0
total = 0
while True:
    inp = raw_input("Enter a number:")
    if inp == 'done': break
    if len(inp) < 1: break
    try:
        num = float(inp)
    except:
        print "Invaild input"
        continue
    count = count + 1
    total = total + num
    print num, total, count

print "Average:", total / count
