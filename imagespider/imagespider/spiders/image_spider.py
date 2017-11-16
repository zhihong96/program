# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector

from imagespider.items import ImagespiderItem

class Imagespider(Spider):
    name="image"
    start_urls=[
        'http://tieba.baidu.com/p/4023230951']

    def parse(self, response):
        sel=Selector(response)

        image_urls = sel.xpath('//div[@id="post_content_75283192143"]/img[@class="BDE_Image"]/@src').extract()
        #print 'urls:', image_urls

        item=ImagespiderItem()
        item['image_urls'] = image_urls

        yield item
