# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TelekomItemsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tarif = scrapy.Field()
    grundpreis = scrapy.Field()
    bereitstellungspreis = scrapy.Field()
    dauer = scrapy.Field()
    mms = scrapy.Field()
    datennutzung = scrapy.Field()
    geschwindigkeit_down = scrapy.Field()
    geschwindigkeit_up = scrapy.Field()
    datenvolumen = scrapy.Field()


