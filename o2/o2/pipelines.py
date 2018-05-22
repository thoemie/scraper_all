# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exporters import JsonItemExporter, JsonLinesItemExporter

class O2Pipeline(object):
    # # Variante 1

    def open_spider(self, spider):
        self.file = open('plans.json', 'wb')
        self.exporter = JsonItemExporter(self.file)
        self.file.write(b'{"Tariffs":')
        self.exporter.start_exporting()
        # self.file.write('\n')
        # self.file.write('[')

    def close_spider(self, spider):
        # self.file.write(b']')
        # self.file.write('\n')
        # self.file.write('\n')
        self.exporter.finish_exporting()
        self.file.write(b'}')
        self.file.close()

    def process_item(self, item, spider):
        # for n in item:
        #     str(n).replace(',','.')
        # line = json.dumps(dict(item), indent=4) #separators=(',', ':'))
        # self.file.write(line)
        self.exporter.export_item(item)
        return item
    # Variante 1 ENDE //

    # # Variante 2
    # file = None

    # def open_spider(self, spider):
    #     self.file = open('item.json', 'wb')
    #     self.exporter = JsonItemExporter(self.file)
    #     # self.file.write('{"Tariffs":')
    #     self.exporter.start_exporting()

    # def close_spider(self, spider):
    #     self.exporter.finish_exporting()
    #     # self.file.write('}')
    #     self.file.close()

    # def process_item(self, item, spider):
    #     self.exporter.export_item(item)
    #     return item
    # # Variante 2 Ende //

    
    # # Variante 3 - geht iwie nicht
    # def __init__(self):
    #     #Instantiate API Connection
    #     self.files = {}
        
    # def spider_opened(self, spider):
    #     #open a static/dynamic file to read and write to
    #     file = open('%s_items.json' % spider.name, 'w+b')
    #     self.files[spider] = file
    #     file.write('''{
    # "product": [''')
    #     self.exporter = JsonLinesItemExporter(file)
    #     self.exporter.start_exporting()

    # def spider_closed(self, spider):
    #     self.exporter.finish_exporting()
    #     file = self.files.pop(spider)
    #     file.write("]}")
    #     file.close()
    # # Variante 3 Ende