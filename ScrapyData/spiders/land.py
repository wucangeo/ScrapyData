# -*- coding: utf-8 -*-
import os, sys

from scrapy.spiders import Spider
from scrapy.selector import Selector

from ScrapyData.items import Website


class LandSpider(Spider):
    name = "land"
    allowed_domains = ["tuliu.com"]
    start_urls = [
        "http://pinggu.tuliu.com/view-368720.html"
    ]

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

            names = site.xpath('string(dl/dd[1]/p[2]/a/text())').extract()
            nameitem = []
            for name in names:
                nameitem.append(name.encode('unicode-escape'))
            item['name'] = nameitem
            item['url'] = site.xpath('string(dl/dd[2]/p[2]/a/text())').extract()
            item['description'] = site.xpath('string(dl/dd[3]/p[2]/text())').extract()
            items.append(item)

        return items
