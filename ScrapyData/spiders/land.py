# -*- coding:utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exporters import JsonItemExporter

from scrapy.spiders import Spider
from scrapy.selector import Selector
from ScrapyData.items import Website

class LandSpider(Spider):
    name = "land"
    allowed_domains = ["tuliu.com"]
    # start_urls = [
    #     "http://pinggu.tuliu.com/view-368720.html"
    # ]
    start_urls = [
        "http://tuliu.com/view-372131.html"
    ]
    # 获取100条
    # initUrl = "http://tuliu.com/view-3721"
    # for i in range(100):
    #     url = initUrl + str(i).zfill(2) + ".html"
    #     print(url)
    #     start_urls.append(url)

    # 获取10条
    initUrl = "http://tuliu.com/view-37213"
    for i in range(10):
        url = initUrl + str(i) + ".html"
        print(url)
        start_urls.append(url)

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html
        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath('//div[@class="attribute"]')
        items = []

        for site in sites:
            item = Website()

            # names = site.xpath('string(dl/dd[1]/p[2]/a/text())').extract()
            # nameitem = []
            # for name in names:
            #     nameitem.append(name.encode('unicode-escape'))
            item['name'] = site.xpath('string(dl/dd[1]/p[2]/a/text())').extract()
            item['url'] = site.xpath('string(dl/dd[2]/p[2]/a/text())').extract()
            item['description'] = site.xpath('string(dl/dd[3]/p[2]/text())').extract()
            items.append(item)

        return items