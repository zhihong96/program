# -*- coding: utf-8 -*-

import urllib
import re
from bs4 import BeautifulSoup

url = raw_input('Enter url:')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print tag.get('href',None)
