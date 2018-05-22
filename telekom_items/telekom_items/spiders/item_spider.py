
import scrapy
from scrapy import Request
from urllib.parse import urljoin
from scrapy.loader import ItemLoader
import unicodedata
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import replace_escape_chars
from telekom_items.items import TelekomItemsItem

class TelekomSpider(scrapy.Spider):
    name = "telekom_loader"
    start_urls = [
        'https://www.telekom.de/unterwegs/tarife-und-optionen/smartphone-tarife'
    ]


    def parse(self, response):
        for follow_url in response.css(".t7::attr(href)").extract():
            url = response.urljoin(follow_url)
            yield Request(url, callback=self.populate_item)
        

    def populate_item(self, response):
        l = ItemLoader(item=TelekomItemsItem(), response=response)
        l.default_input_processor = MapCompose(str.strip)
        l.default_output_processor = TakeFirst()

        l.add_css('tarif', ".page-title::text")
        l.add_xpath('grundpreis', '//*[@class="row"]/table//tr[contains(., "Monatlich")]/td[2]/strong/text()')
        l.add_xpath('bereitstellungspreis', '//*[@class="row"]/table//tr[contains(., "Einmalig")]/td[2]/strong/text()')
        l.add_xpath('dauer', '//*[@class="row"]/table//tr[contains(., "Dauer")]/td[2]/strong/text()')
        l.add_xpath('mms', '//*[@class="row"]/table//tr[contains(., "MMS")]/td[2]/strong/text()')
        l.add_xpath('datennutzung', '//*[@class="row"]/table//tr[contains(., "Datennutzung")]/td[2]/strong/text()')
        l.add_xpath('geschwindigkeit_down', '//*[@class="row"]/table//tr[contains(., "Download")]/td[2]/strong/text()')
        l.add_xpath('geschwindigkeit_up', '//*[@class="row"]/table//tr[contains(., "Upload")]/td[2]/strong/text()')
        l.add_xpath('datenvolumen', '//*[@class="row"]/table//tr[contains(., "Highspeed-Volumen")]/td[2]/strong/text()')
        


        
        
        yield l.load_item()







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
