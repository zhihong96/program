# -*- coding: utf-8 -*-

import re
import urllib2
import requests
import os
import cookielib
import sys

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/62.0.3202.62 Chrome/62.0.3202.62 Safari/537.36'}
url = 'http://www.imooc.com'
#url = 'http://image.so.com'
proxies = {
    'http': 'http://111.62.251.66:80',
    'https': 'https://111.62.251.66:80'}
s = requests.Session()
#s.cookies = cookielib.LWPCookieJar(filename='cookies')

# get html
def getHtml(url):
    #page = urllib2.urlopen(url)
    page = s.get(url, headers=headers)
    #html = page.read()
    html = page.content
    #html = page.text
    #print html
    return html


# get img url     
def getAllimg(html):
    #reg = r'<img.*?src="(.*?)".*?/>'
    reg = r'src="//(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    new_imglist = ["http://" + add for add in imglist]
    print new_imglist
    return new_imglist

# create path
def mkdir(path):
    path = path.strip()
    # if path exists,return true,if not,return false.
    isExists = os.path.exists(path)
    if not isExists:
        print 'create new folder'
        os.makedirs(path)
        return True
    else:
        print 'success create'
        return False

# save file
def saveFile(new_imglist, name):
    i = 0
    for imgUrl in new_imglist:
        splitPath = imgUrl.split('.')# 将path分割成目录和文件名二元组返回
        fTail = splitPath.pop() #pop:移除最后一个元素，并返回该值
        if len(fTail) > 3:
            fTail = 'jpg'
        fileName = name + "/" + str(i) + '.' + fTail
        f = open(fileName, 'wb')
        #f = open(str(i)+'.jpg', 'wb')
        req = s.get(imgUrl,headers=headers).content
        f.write(req)
        f.close
        i += 1

if __name__=='__main__':
    html = getHtml(url)
    path = 'image'
    mkdir(path)
    new_imglist = getAllimg(html)
    saveFile(new_imglist, path)
