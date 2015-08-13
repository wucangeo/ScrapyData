__author__ = 'land'
# -*- coding:utf-8 -*-
try:
    import json
except ImportError:
    import simplejson as json
from pprint import pprint
import codecs
import sys
import chardet

input_file = file('data4.json', 'r')

f = open("data4.json").read()
# jsonObj = [url.strip() for url in f.readlines()]
dataset = json.loads(input_file.read().decode("utf-8-sig"))
# pprint(jsonObj)
# pprint(dataset)

for data in dataset:
    namelist = data['name']
    for name in namelist:
        pprint(type(name))
        pprint(name)
        result = codecs.encode(name, 'utf-8')
        pprint(result)

# f.close()


    def to_unicode_or_bust(obj, encoding='utf-8'):
        if isinstance(obj, basestring):
            if not isinstance(obj, unicode):
                obj = unicode(obj, encoding)
        return obj
