# -*- coding: utf-8 -*-

try:
    inp = raw_input("enter hours:")
    hours = float(inp)
    inp = raw_input("enter rate:")
    rate = float(inp)
    print hours, rate
    if hours <= 40:
        pay = hours * rate
    else:
        pay = rate * 40 + (rate * 1.5 * (hours - 40))
    print pay
except:
    print "Error, please enter numeric input"
    quit()

print pay

