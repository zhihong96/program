# -*- coding: utf-8 -*-

import math 

# pointe as lists

def addPoints(p1, p2):
    r=[]
    r.append(p1[0] + p2[0])
    r.append(p1[1] + p2[1])
    return r

p = [1,2]
q = [3,1]
r = addPoints(p,q)
print r

# points as classes

class caratesianPoint:
    pass

cp1= caratesianPoint()
cp2 = caratesianPoint()
cp1.x = 1.0
cp1.y = 2.0
cp2.x = 1.0
cp2.y = 3.0

def samePoint(p1,p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

def printPoint(p):
    print '(' + str(p.x) + ', ' + str(p.y) + ')'

def polarPoint():
    pass

    pp1 = polarPoint()
    pp2 = polarPoint()
    pp1.radius = 1.0
    pp1.angle = 0
    pp2.radius = 2.0
    pp2.angle = math.pi / 4.0

class cPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = math.sqrt(self.x*self.x + self.y*self.y)
        self.angle = math.atan2(self.y, self.x)

    def caratesian(self):
        return (self.x, self.y)
    def polar(self):
        return (self.radius, self.angle)
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    def __cmp__(self, other):
        return (self.x > other.x) and (self.y > other.y)
p = cPoint(1.0, 2.0)
print p.x
print p.caratesian()
p.radius = 1.0
print p.polar()
q = cPoint(3.0, 4.0)
print p > q
print dir(p)
