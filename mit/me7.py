# -*- coding: utf-8 -*-

import math

#get base
inputOK=False
while not inputOK:
    base = input('Enter base: ')
    if type(base) == type(1.0): inputOK = True
    else: print('Error. Base must be floating point number.')

#Get Height
inputOK = False
while not inputOK:
    height = input('Enter height: ')
    if type(height) == type(1.0): inputOK = True
    else: print('Error. Height must be floating point number.')
hyp = math.sqrt(base*base + height*height)
print 'Base: '+str(base)+',height: '+str(height)+', hyp: '+ str(hyp)
def getFloat(requestMsg, errorMsg):
    inputOK = False
    while not inputOK:
        val = input(requestMsg)
        if type(val) == type(1.0): inputOK = True
        else: print(errorMsg)
    return val

base = getFloat('Enter base: ', 'Error: base must be a float')
height = getFloat('Enter height: ', 'Error: height must be a float')

hyp = math.sqrt(base*base + height*height)

print 'Base: ' + str(base) + ',height: ' + str(height) + ', hyp:' + str(hyp)
