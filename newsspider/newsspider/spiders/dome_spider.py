# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector
from newsspider.items import DomeItem

class DomeSpider(Spider):
    name = "dome"
    allowed_domains = ["people.com"]
    start_urls = [
          "http://www.people.com.cn/",
          "http://politics.people.com.cn/ywkx/",
"http://www.people.com.cn/GB/59476/"  
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul/li')
        items = []
        for site in sites:
            item = DomeItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('text()').extract()
            items.append(item)
        return items
