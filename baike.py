# -*- coding: utf-8 -*-

import urllib2
import urllib
import re
import thread
import time
import json

# 加载处理糗事百科
class Spider_Model:
    
    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False

    # 获取内容，添加到列表并返回
    def GetPage(self, page):
        myUrl = 'http://m.qiushibaike.com/hot/page/' + page
        user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/62.0.3202.62 Chrome/62.0.3202.62 Safari/537.36'
        headers = {'User-Agent' : user_agent}
        req = urllib2.Request(myUrl, headers=headers)
        #print myUrl
        myResponse = urllib2.urlopen(req)
        myPage = myResponse.read()
        #print myPage
        # encode的作用是将unicode编码转换成其他编码的字符串
        # decode的作用是家其他编码的字符串转换成unicode编码
        unicodePage = myPage.decode("utf-8")
        #print unicodePage
        # 找出所有class="content"的div标记
        # re.S是任意匹配模式，也就是.可以匹配换行符
        myItems = re.findall(r'<div.*?class="content">\n+<span>(.*?)</span>\n+</div>',unicodePage, re.S)
        items = []
        #print myItems
       # for item in myItems:
            # item 中第一个是div的标题，也就是时间
            # item 中第二个是div的内容，也就是内容
          # items.appen([item[0].replace("\n",""),item[1].replace("\n","")])
        return myItems

    # 用于加载新内容
    def LoadPage(self):
        # 如果用户未输入quit则一直运行
        while self.enable:
            # 如果pages数组中的内容小于2个
            if len(self.pages) < 2:
                try:
                    # 获取新的页面
                    myPage = self.GetPage(str(self.page))
                    self.page += 1
                    self.pages.append(myPage)
                except:
                    print 'error'
            else:
                time.sleep(5)

    def ShowPage(self, nowPage, page):
        i = 1
        for i in range(1,len(nowPage)):
            if i < len(nowPage):
                # replace:把'<br\>'替换为'\n'换行符
                oneStory = nowPage[i].replace('<br\>','\n')
                print u'第%d页,第%d个故事' %(page, i), oneStory
                i += 1
            else:
                break
        myInput = str(raw_input('回车查看下一页，按quit退出：\n'))
        if myInput == 'quit':
            self.enable = False

    def Start(self):
        self.enable = True
        page = self.page
        print '加载中'
        # 新建一个线程在后台加载并储存
        thread.start_new_thread(self.LoadPage,())
        # 加载处理
        while self.enable:
            # 如果self的page数组中存有元素
            if self.pages:
                nowPage = self.pages[0]
                del self.pages[0]
                self.ShowPage(nowPage, page)
                page += 1

if __name__=='__main__':
    print '回车'
    raw_input(' ')
    myModel = Spider_Model()
    myModel.Start()
 
