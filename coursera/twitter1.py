# -*- coding: utf-8 -*-

import urllib
import twurl
import json

twitter_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

while True:
    print ''
    acct = raw_input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(twitter_url,
        {'screen_name': acct, 'count': '5'})
    print 'Retrieing', url
    connection = urllib.urlopen(url)
    data = connection.read()
    #print data[:250]
    headers = connection.info().dict
    # print headers
    print 'Remaining', headers['x-rate-limit-remaining']
    js = json.loads(data)
    print json.dumps(js, indent=4)

    for u in js['users']:
        print u['screen_name']
        s = u['status']['text']
        print '    ', s[:50]
