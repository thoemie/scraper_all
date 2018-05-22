# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exporters import JsonItemExporter, JsonLinesItemExporter

class O2NoLoaderPipeline(object):


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
