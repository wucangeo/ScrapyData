# -*- coding:utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector

from ScrapyData.items import Website


class LandSpider(Spider):
    name = "land"
    allowed_domains = ["beijing.tuliu.com"]
    start_urls = [
        "http://beijing.tuliu.com/list-pg1.html#sub_list_b"
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath('//div[@class="sortlist_cont"]')
        items = []

        for site in sites:
            item = Website()

            item['name'] = site.xpath('div[@class="box2"]/text()').extract()
            item['url'] = site.xpath('div[@class="box1"]//p[@class="txt1"]/text()').extract()
            item['description'] = "bbb"
            items.append(item)

        return items
