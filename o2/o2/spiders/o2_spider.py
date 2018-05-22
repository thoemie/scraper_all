# This is telekom_spider.py in //.../myScrapyProject/myScrapyProject/spiders
import scrapy
from scrapy import Request
from urllib.parse import urljoin
from scrapy.loader import ItemLoader
import unicodedata
from scrapy.loader.processors import MapCompose, TakeFirst
#from w3lib.html import replace_escape_chars
from o2.items import O2Item
from scrapy.loader.processors import Join
from decimal import Decimal
import locale


class O2Spider(scrapy.Spider):

    name = "o2spider"
    start_urls = [
        'https://www.o2online.de/tarife/'
    ]


    def parse(self, response):
        for follow_url in response.xpath("//a[contains(@title, 'Tarif wählen')]/@href").extract():
            url = response.urljoin(follow_url)
            yield Request(url, callback=self.populate_item)
        

    def populate_item(self, response):
        l = ItemLoader(item=O2Item(), response=response)
        l.default_input_processor = MapCompose(str.strip)
        l.default_output_processor = Join(' ')
        
        

        l.add_css('tarif', ".tariffProductName::attr(value)")

        # grundpreis_euro = response.xpath('//span[contains(., "monatlich")]/following-sibling::*[contains(@class, "sum")]//text()').extract()
        # grundpreis_cent = response.xpath('//span[contains(., "monatlich")]/following-sibling::*[contains(@class, "suffix")]//text()').extract()
        # grundpreis = str(grundpreis_euro) + ',' + str(grundpreis_cent) + '€'
        #l.add_value('grundpreis', grundpreis)
        # l.add_xpath('grundpreis', '//span[contains(., "monatlich")]/following-sibling::*[contains(@class, "sum")]//text()')
        # l.add_xpath('grundpreis', '//span[contains(., "monatlich")]/following-sibling::*[contains(@class, "suffix")]//text()')


        grundpreis_wert = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "), " tariff-details-property ")]/div[@class="tariff-information-table"]//*[contains(., "Monatliche Grundgebühr")]/following-sibling::*/div/span/text()').re("[0-9,.]+")

 

        # for n in grundpreis_wert:
        #     n.replace(',','.')

        # for i in grundpreis_wert:
        #     i = float(i)

        l.add_value('grundpreis', grundpreis_wert)
        # l.add_xpath('grundpreis', '//*[contains(concat(" ", normalize-space(@class), " "), " tariff-details-property ")]/div[@class="tariff-information-table"]//*[contains(., "Monatliche Grundgebühr")]/following-sibling::*/div/span/text()')
        
        #l.add_xpath('bereitstellungspreis', '//*[contains(concat(" ", normalize-space(@class), " "), " tariff-details-property ")]/div[@class="tariff-information-table"]//*[contains(., "Anschlusspreis")]/following-sibling::*/following-sibling::*//span/text()')
        bereitstellungspreis_wert = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "), " tariff-details-property ")]/div[@class="tariff-information-table"]//*[contains(., "Anschlusspreis")]/following-sibling::*/following-sibling::*//span/text()').re("[0-9,.]+")
          
        

        l.add_value('bereitstellungspreis', bereitstellungspreis_wert)

        # l.add_xpath('dauer', '//*[@class="row"]/table//tr[contains(., "Dauer")]/td[2]/strong/text()')

        #minute_wert = response.xpath('string(//*[@class="tariff-description"]/article[4]/div/div/table/tbody/tr[1]/td[2]/strong/text())').re("[0-9,.€ ]+")
        minute_wert = response.xpath('string(//*[contains(., "Gespräche:")]/following-sibling::*/strong/text())').re("[0-9,.]+")
        l.add_value('minute', minute_wert)

        sms_wert = response.xpath('string(//*[contains(., "SMS:")]/following-sibling::*/strong/text())').re("[0-9,.]+")
        l.add_value('sms', sms_wert)

        mms_wert = response.xpath('string(//*[contains(., "MMS:")]/following-sibling::*/text())').re("[0-9,.]+")
        l.add_value('mms', mms_wert)

        # l.add_xpath('datennutzung', '//*[@class="row"]/table//tr[contains(., "Datennutzung")]/td[2]/strong/text()')
        # l.add_xpath('geschwindigkeit_down', '//*[@class="row"]/table//tr[contains(., "Download")]/td[2]/strong/text()')
        # l.add_xpath('geschwindigkeit_up', '//*[@class="row"]/table//tr[contains(., "Upload")]/td[2]/strong/text()')
        l.add_xpath('datenvolumen', '//div[@id="tariff-carousel"]//div[@data-ng-bind-html="tariff.tariffFeatures.feature1 | coUnsafeHtml"]//span/text()')
        
        yield l.load_item()

# //*[(contains(concat(" ", normalize-space(@class), " "), " value ")) and (contains(concat(" ", normalize-space(@class), " "), " ng-binding "))]
# value ng-binding





    # This selector matches the class "t7" which is used for the Link to the "Tarifdetails" and extracts the href-Attribute
#     plans = response.css(".t7::attr(href)").extract()
    
#     for p in plans:
#         # Somehow joins / concatenates each entry in plans (which are relative paths) together with the first part of the URL and returns the whole URL
#         url = urljoin(response.url, p)
#         yield scrapy.Request(url, callback=self.parse_plan)

# def parse_plan(self, response):

#     l = TrimItemLoader(selector=response)
#     l.add_css('tarif', ".page-title::text.extract()")
#     l.add_xpath('grundpreis', '//*[@class="row"]/table//tr[contains(., "Monatlich")]/td[2]/strong/text().extract()')
#     l.add_xpath('bereitstellungspreis', '//*[@class="row"]/table//tr[contains(., "Einmalig")]/td[2]/strong/text().extract()')
#     l.add_xpath('dauer', '//*[@class="row"]/table//tr[contains(., "Dauer")]/td[2]/strong/text().extract()' )
#     l.add_xpath('mms', '//*[@class="row"]/table//tr[contains(., "MMS")]/td[2]/strong/text().extract()' )
#     l.add_xpath('datennutzung', '//*[@class="row"]/table//tr[contains(., "Datennutzung")]/td[2]/strong/text().extract()' )
#     l.add_xpath('geschwindigkeit_down', '//*[@class="row"]/table//tr[contains(., "Download")]/td[2]/strong/text().extract()')
#     l.add_xpath('geschwindigkeit_up', '//*[@class="row"]/table//tr[contains(., "Upload")]/td[2]/strong/text().extract()' )
#     l.add_xpath('datenvolumen', '//*[@class="row"]/table//tr[contains(., "Highspeed-Volumen")]/td[2]/strong/text().extract()' )
#     return l.load_item()
