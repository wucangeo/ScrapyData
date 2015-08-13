# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from scrapy.exceptions import DropItem


class FilterWordsPipeline(object):

    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    words_to_filter = ['politics', 'religion']

    def process_item(self, item, spider):
        for word in self.words_to_filter:
            if word in unicode(item['description']).lower():
                raise DropItem("Contains forbidden word: %s" % word)
        else:
            return item

# class JsonWriterPipeline(object):
#     def __init__(self):
#         self.file = codecs.open('item.json','w',encoding='utf-8')

#     def process_item(self,item,spider):
#         line = json.dumps(dict(item))
#         self.file.write(line.decode('unicode_escape'))
#         return item


class JsonWriterPipeline(object):

    # def __init__(self):
    #     self.file = codecs.open('items.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):

        line = json.dumps(dict(item))
        self.file.write(line.decode('unicode_escape'))
        return item
