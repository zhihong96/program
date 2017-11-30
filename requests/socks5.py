# -*- coding: utf-8 -*-

import urllib2
import requests
import socks, socket
from sockshandler import SocksiPyHandler

url ='https://www.google.com/'
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/62.0.3202.62 Chrome/62.0.3202.62 Safari/537.36'}
proxies = {
    'http': 'socks5://127.0.0.1:1080',
    'https': 'socks5://127.0.0.1:1080'
}

def requestsproxy():
    response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
    #print response.text
    print response.status_code
    print response.headers

def urllib2proxy():
    proxy = urllib2.ProxyHandler({'http': '127.0.0.1:1080','https': '127.0.0.1:1080',})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    response = urllib2.urlopen(url, timeout=10)
    print response.read()

if __name__=='__main__':
    requestsproxy()
