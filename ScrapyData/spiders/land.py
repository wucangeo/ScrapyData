# -*- coding:utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exporters import JsonItemExporter

from scrapy.spiders import Spider
from scrapy.selector import Selector
from ScrapyData.items import Website
import time
import MySQLdb

class LandSpider(Spider):
    def __init__(self):
        # 连接数据库
        self.conn = MySQLdb.connect(host='localhost', user='wucan', passwd='wucan', charset='utf8')
        self.conn.select_db('land')
        self.cur = self.conn.cursor()

    name = "land"
    allowed_domains = ["tuliu.com"]
    start_urls = [
        "http://pinggu.tuliu.com/view-368720.html"
    ]

    # 获取100条
    # initUrl = "http://tuliu.com/view-3721"
    # for i in range(100):
    #     url = initUrl + str(i).zfill(2) + ".html"
    #     print(url)
    #     start_urls.append(url)

    # 获取10条
    initUrl = "http://tuliu.com/view-36872"
    for i in range(1, 10):
        url = initUrl + str(i) + ".html"
        start_urls.append(url)
        # print(url)
    def ConnDB(self):
        self.conn = MySQLdb.connect(host='localhost', user='wucan', passwd='wucan', charset='utf8')
        self.conn.select_db('land')
        self.cur = self.conn.cursor()

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html
        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath('//div[@class="content-table clearfix"]')
        items = []
        data = []

        cururl = response.url
        landtype = ""
        cirproperty = ""
        pubtime = ""
        updatetime = ""
        sumarea = ""
        ciryear = ""
        sumprice = ""
        paytype = ""

        for site in sites:
            item = Website()


            # item['name'] = site.xpath('string(dl/dd[1]/p[2]/a/text())').extract()
            # item['url'] = site.xpath('string(dl/dd[2]/p[2]/a/text())').extract()
            # item['description'] = site.xpath('string(dl/dd[3]/p[2]/text())').extract()
            # items.append(item)
            landtype = site.xpath('string(dl[1]/dd/a/text())').extract()[0]
            cirproperty = site.xpath('string(dl[2]/dd/a/text())').extract()[0]
            pubtime = site.xpath('string(dl[3]/dd/text())').extract()[0]
            updatetime = site.xpath('string(dl[4]/dd/text())').extract()[0]
            sumarea = site.xpath('string(dl[5]/dd/text())').extract()[0]
            ciryear = site.xpath('string(dl[6]/dd/text())').extract()[0]
            sumprice = site.xpath('string(dl[7]/dd/li/text())').extract()[0]
            paytype = site.xpath('string(dl[8]/dd/text())').extract()[0]
            # if len(tname) != 0 or len(tuser) != 0 or len(tdescription) != 0:
            data.extend([landtype, cirproperty, pubtime,updatetime,sumarea,ciryear,sumprice,paytype])

        # return items
        # print "length of data:",len(data)
        if len(data) != 0:
            data.append(cururl)
            print data

            # 处理时间
            # print "testttttt",landtype,cirproperty,pubtime

            self.ConnDB()
            # SQL 插入语句
            sql = "INSERT INTO land(landtype,cirproperty,pubtime,updatetime,sumarea,ciryear,sumprice,paytype,cururl) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            try:
                # 执行sql语句
                self.cur.execute(sql,data)
                # 提交到数据库执行
                self.conn.commit()
                print "insert succ"
            except Exception as e:
                # time.sleep(30)
                print "insert error",type(e), e
                # Rollback in case there is any error
                self.conn.rollback()
            # 关闭数据库连接
            self.conn.close()
        # print data
        # time.sleep(1)
