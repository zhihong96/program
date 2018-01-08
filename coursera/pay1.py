# -*- coding: utf-8 -*-

def computepay(h,r):
    if h <= 40:
        p = h * r
    else:
        p = 40 * r + (r * 1.5 * (h - 40))
    print p
    return p
try:
    inp = raw_input("enter hours:")
    hours = float(inp)
    inp = raw_input("enter rate:")
    rate = float(inp)
except:
    print"Error, please enter numeric input"
    quit()
pay = computepay(hours,rate)
print "we are back", pay
