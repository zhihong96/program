# -*- coding: utf-8 -*- 
import math, random, pylab

class Location(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def move(self, xc, yc):
        return Location(self.x+float(xc), self.y+float(yc))
    def getCoords(self):
        return self.x, self.y
    def getDist(self, other):
        ox, oy = other.getCoords()
        xDist = self.x - ox
        yDist = self.y - oy
        return math.sqrt(xDist**2 + yDist**2)

class CompassPt(object):
    possibles = ('N', 'S', 'E', 'W')
    def __init__(self, pt):
        if pt in self.possibles: self.pt = pt
        else: raise ValueError('in CompassPt.__init__')
    def move(self, dist):
        if self.pt == 'N': return (0, dist)
        elif self.pt == 'S': return (0, -dist)
        elif self.pt == 'E': return (dist, 0)
        elif self.pt == 'W': return (-dist, 0)
        else: raise ValueError('in CompassPt.move')
class Field(object):
    def __init__(self, drunk, loc):
        self.drunk = drunk
        self.loc = loc
    def move(self, cp, dist):
        oldLoc = self.loc
        xc, yc = cp.move(dist)
        self.loc = oldLoc.move(xc, yc)
    def getLoc(self):
        return self.loc
    def getDrunk(self):
        return self.drunk

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def move(self, field, cp, dist = 1):
        if field.getDrunk().name != self.name:
            raise ValueError('Drunk.move called with drunk not in field')
        for i in range(dist):
            field.move(cp, 1)

class UsualDrunk(Drunk):
    def move(self, field, dist = 1):
        cp = random.choice(CompassPt.possibles)
        Drunk.move(self, field, CompassPt(cp), dist) #Note notation of call

class ColdDrunk(Drunk):
    def move(self, field, dist = 1):
        cp = random.choice(CompassPt.possibles)
        if cp == 'S':
            Drunk.move(self, field, CompassPt(cp), 2*dist)
        else:
            Drunk.move(self, field, CompassPt(cp), dist)

class EWDrunk(Drunk):
    def move(self, field, time = 1):
        cp = random.choice(CompassPt.possibles)
        while cp != 'E' and cp != 'W':
            cp = random.choice(CompassPt.possibles)
        Drunk.move(self, field, CompassPt(cp), time)

def performTrial(time, f):
    start = f.getLoc()
    distances = [0.0]
    for t in range(1, time + 1):
        f.getDrunk().move(f)
        newLoc = f.getLoc()
        distance = newLoc.getDist(start)
        distances.append(distance)
    return distances

def performSim(time, numTrials, drunkType):
    distLists = []
    for trial in range(numTrials):
        d = drunkType('Drunk' + str(trial))
        f = Field(d, Location(0, 0))
        distances = performTrial(time, f)
        distLists.append(distances)
    return distLists

def ansQuest(maxTime, numTrials, drunkType, title):
    means = []
    distLists = performSim(maxTime, numTrials, drunkType)
    for t in range(maxTime + 1):
        tot = 0.0
        for distL in distLists:
            tot += distL[t]
        means.append(tot/len(distLists))
    pylab.figure()
    pylab.plot(means)
    pylab.ylabel('distance')
    pylab.xlabel('time')
    pylab.title(title)
    

maxTime = 500
numTrials = 100
ansQuest(maxTime, numTrials, UsualDrunk, 'UsualDrunk')
ansQuest(maxTime, numTrials, ColdDrunk, 'clodDrunk')
ansQuest(maxTime, numTrials, EWDrunk, 'EWDrunk')
pylab.show()
