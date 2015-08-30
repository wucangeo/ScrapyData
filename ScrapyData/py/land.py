
# -*- coding:utf-8 -*-
# 把str编码由ascii改为utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import MySQLdb
import time

# import scrapy
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
# from scrapy.exporters import JsonItemExporter

from scrapy.spiders import Spider
from scrapy.selector import Selector
from ScrapyData.items import Website

class LandSpider(Spider):
    def __init__(self):
        # 连接数据库
        self.conn = MySQLdb.connect(host='localhost', user='root', passwd='noroot', charset='utf8')
        self.cur = self.conn.cursor()
        self.conn.select_db('crawldata')

    name = "land"
    allowed_domains = ["tuliu.com"]
    # start_urls = [
    #     "http://pinggu.tuliu.com/view-368720.html"
    # ]
    start_urls = [
        "http://tuliu.com/view-372121.html"
        ]

    # 获取100条
    # initUrl = "http://tuliu.com/view-3721"
    # for i in range(100):
    #     url = initUrl + str(i).zfill(2) + ".html"
    #     print(url)
    #     start_urls.append(url)

    # 获取10条
    initUrl = "http://tuliu.com/view-37212"
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
            # time.sleep(5)
            try:
                # item = []

                # names = site.xpath('string(dl/dd[1]/p[2]/a/text())').extract()
                # nameitem = []
                # for name in names:
                #     nameitem.append(name.encode('unicode-escape'))
                # item['siteid'] = index
                tname = site.xpath('string(dl/dd[1]/p[2]/a/text())').extract()[0]
                turl = site.xpath('string(dl/dd[2]/p[2]/a/text())').extract()[0]
                description = site.xpath('string(dl/dd[3]/p[2]/text())').extract()[0]
                items.append((tname,turl,description))
            # 少数数据不规则，可能导致异常，此时直接忽略
            except IndexError:
                pass
            except MySQLdb.connector.ProgrammingError as ex:
                if self.cur:
                    print "\n".join(self.cur.messages)
                    # You can show only the last error like this.
                    # print cursor.messages[-1]
                else:
                    print "\n".join(self.conn.messages)
                    # Same here you can also do.
                    # print self.db.messages[-1]
            except Exception as e:
                #time.sleep(30)
                print type(e),e
                time.sleep(120)

        print items

        return items
        # # 15本书籍处理完之后，执行一次批量插入操作
        # sql = "INSERT INTO land (tname, turl, description) VALUES (%s, %s, %s)"
        # #
        # self.cur.executemany(sql, items)
        # # 每个标签下的书籍处理完后提交一次
        # self.conn.commit()
        # # # 收尾工作，关闭数据库连接
        # self.cur.close()
        # self.conn.close()
