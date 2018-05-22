# This is telekom_spider.py in //.../myScrapyProject/myScrapyProject/spiders
import scrapy
from urllib.parse import urljoin
from telekom_1.items import Telekom1Item

class TelekomSpider(scrapy.Spider):
    name = "telekom_spider"
    start_urls = [
        'https://www.telekom.de/unterwegs/tarife-und-optionen/smartphone-tarife'
    ]



    def parse(self, response):
        # This selector matches the class "t7" which is used for the Link to the "Tarifdetails" and extracts the href-Attribute
        plans = response.css(".t7::attr(href)").extract()
        
        for p in plans:
            # Somehow joins / concatenates each entry in plans (which are relative paths) together with the first part of the URL and returns the whole URL
            url = urljoin(response.url, p)
            yield scrapy.Request(url, callback=self.parse_plan)

    
    def parse_plan(self, response):
                
        # this is the container for the HTML-Table with the detailed pricing information
        for info in response.css(".tariff-details.container-fixed"):


            product = Telekom1Item()
            product['tarif'] = str.strip(info.css(".page-title::text").extract_first())
            product['grundpreis'] = str.strip(info.xpath('//*[@class="row"]/table//tr[contains(., "Monatlich")]/td[2]/strong/text()').extract_first())
            product['bereitstellungspreis'] = str.strip(info.xpath('//*[@class="row"]/table//tr[contains(., "Einmalig")]/td[2]/strong/text()').extract_first())
            product['dauer'] = str.strip(info.xpath('//*[@class="row"]/table//tr[contains(., "Dauer")]/td[2]/strong/text()').extract_first())
            product['mms'] = str.strip(info.xpath('//*[@class="row"]/table//tr[contains(., "MMS")]/td[2]/strong/text()').extract_first())
            product['sms'] = float(0.00)
            product['minute'] = float(0.00)
            # product['datennutzung = str.strip(info.xpath('//*[@class="row"]/table//tr[contains(., "Datennutzung")]/td[2]/strong/text()').extract_first())
            # product['geschwindigkeit_down = str.strip(info.xpath('//*[@class="row"]/table//tr[contains(., "Download")]/td[2]/strong/text()').extract_first())
            # product['geschwindigkeit_up = str.strip(info.xpath('//*[@class="row"]/table//tr[contains(., "Upload")]/td[2]/strong/text()').extract_first())
            product['datenvolumen'] = str.strip(info.xpath('//*[@class="row"]/table//tr[contains(.,"Highspeed-Volumen")]/td[2]/strong/text()').extract_first())
           
            yield product



            # yield {
            #     # Selectors match the second bold text nodes in HTML-Table-Data-Cell-nodes in the class "row", that are in the table, whose row contains the provided string (like "Monatlich"). Or the like. Fuck Selectors.
            #     'Tarif' : str.strip(info.css(".page-title::text")).extract_first(),
            #     'Grundpreis' : str.strip(info.xpath('//*[@class="row"]/table//tr[contains(., "Monatlich")]/td[2]/strong/text()')).extract_first(),
            #      'Bereitstellungspreis' : str.strip(info.xpath('//*[@class="row"]/table//tr[contains(., "Einmalig")]/td[2]/strong/text()')).extract_first(),
            #      'Dauer' : str.strip(info.xpath('//*[@class="row"]/table//tr[contains(., "Dauer")]/td[2]/strong/text()')).extract_first(),
            #      'MMS' : str.strip(info.xpath('//*[@class="row"]/table//tr[contains(., "MMS")]/td[2]/strong/text()')).extract_first(),
            #      'Datennutzung' : str.strip(info.xpath('//*[@class="row"]/table//tr[contains(., "Datennutzung")]/td[2]/strong/text()')).extract_first(),
            #      'Geschwindigkeit Download' : str.strip(info.xpath('//*[@class="row"]/table//tr[contains(., "Download")]/td[2]/strong/text()')).extract_first(),
            #      'Geschwindigkeit Upload' : str.strip(info.xpath('//*[@class="row"]/table//tr[contains(., "Upload")]/td[2]/strong/text()')).extract_first(),
            #      'Datenvolumen' : str.strip(info.xpath('//*[@class="row"]/table//tr[contains(., "Highspeed-Volumen")]/td[2]/strong/text()')).extract_first(),

            # }
        