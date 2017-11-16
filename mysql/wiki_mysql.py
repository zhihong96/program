# -*- coding: utf-8 -*-

import urllib2
import re
from bs4 import BeautifulSoup
import pymysql.cursors

# 请求url并把结果转换为utf-8编码
resp=urllib2.urlopen("https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol").read().decode("utf-8")
# use BeautifulSoup parser
soup=BeautifulSoup(resp,"html.parser")

# 获取所有以/wili/开头的a标签的href属性
listUrls=soup.find_all("a",href=re.compile('^/wiki/'))
# 输出所有的词条对应的名称和url
for url in listUrls:
    # 过滤.jps或.JPG结尾的url
    if not re.search("\.(jpg|JPG)$",url["href"]):
        # 输出url的文字和对应的链接
        print url.get_text(),"<-- -->","https://en.wikipedia.org" + url["href"]
        # 获取数据库链接
        connection=pymysql.connect(host='localhost',
            port=3306,
            user='root',
            passwd='****',
            db='testdata',
            charset='utf8')
        try:
            # 获取会话指针
            cur=connection.cursor()
            # 创建sql语句
            sql = "insert into urls(urlname,urlhref) values(%s,%s)"
            # 执行sql语句
            cur.execute(sql,(url.get_text(),"https://en.wikipedia.org" + url["href"]))
             # 提交
            connection.commit()
        finally:
            connection.close()
