# -*- coding: utf-8 -*-

import json

input = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } , 
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(input)
print 'User count:', len(info)

for item in info:
    print "name", item['name']
    print 'id', item['id']
    print 'Attribute', item['x']

