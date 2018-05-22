# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class O2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    providername = scrapy.Field()
    tarif = scrapy.Field()
    grundpreis = scrapy.Field()
    bereitstellungspreis = scrapy.Field()
    sms = scrapy.Field()
    mms = scrapy.Field()
    minute = scrapy.Field()
    datenvolumen = scrapy.Field()

