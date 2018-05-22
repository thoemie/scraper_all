# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import json
# from telekom_1 import items

from scrapy.exporters import JsonItemExporter
import json


# class Telekom1ItemExporter(JsonItemExporter):

#     def __init__(self, file, **kwargs):
#         # To initialize the object we use JsonItemExporter's constructor
#         super().__init__(file)

#     def start_exporting(self):
#         self.file.write(b'{\'product\': [')

#     def finish_exporting(self):
#         self.file.write(b'\n]}')

import json

class Telekom1Pipeline(object):



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


    # def open_spider(self, spider):
    #     self.file = open('plans.json', 'w')

    # def close_spider(self, spider):
    #     self.file.close()

    # def process_item(self, item, spider):
    #     line = json.dumps(dict(item), indent=4, separators=(',', ':')) + ",\n"
    #     self.file.write(line)
    #     return item

# class Telekom1Pipeline(object):
#     def __init__(self, file_name):
#         # Storing output filename
#         self.file_name = file_name
#         # Creating a file handle and setting it to None
#         self.file_handle = None

#     @classmethod
#     def from_crawler(cls, crawler):
#         # getting the value of FILE_NAME field from settings.py
#         output_file_name = crawler.settings.get('FILE_NAME')

#         # cls() calls FanExportPipeline's constructor
#         # Returning a FanExportPipeline object
#         return cls(output_file_name)

#     def open_spider(self, spider):
#         print('Custom export opened')

#         # Opening file in binary-write mode
#         file = open(self.file_name, 'wb')
#         self.file_handle = file

#         # Creating a FanItemExporter object and initiating export
#         self.exporter = Telekom1ItemExporter(file)
#         self.exporter.start_exporting()

#     def close_spider(self, spider):
#         print('Custom Exporter closed')

#         # Ending the export to file from FanItemExport object
#         self.exporter.finish_exporting()

#         # Closing the opened output file
#         self.file_handle.close()

#     def process_item(self, item, spider):
#     #     # passing the item to FanItemExporter object for expoting to file
#         self.exporter.export_item(item)
#         return item





#     def open_spider(self, spider):
#         self.file = open('pipeline_plans.json', 'wb')
#         self.file.write("[")

#     def close_spider(self, spider):
#         self.file.write("]")
#         self.file.close()

#     def process_item(self, product, spider):
#         line = json.dumps(
#             dict(product),
#             sort_keys=True,
#             indent=4,
#             separators=(',', ': ')
#         ) + ",\n"

#         self.file.write(line)
#         return produc
#         pass