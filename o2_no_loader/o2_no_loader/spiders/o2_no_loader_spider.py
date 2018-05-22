# This is telekom_spider.py in //.../myScrapyProject/myScrapyProject/spiders
import scrapy
from urllib.parse import urljoin
from o2_no_loader.items import  O2Item

class TelekomSpider(scrapy.Spider):
    name = "o2noloader"
    start_urls = [
        'https://www.o2online.de/tarife/'
    ]



    def parse(self, response):
        # This selector matches the class "t7" which is used for the Link to the "Tarifdetails" and extracts the href-Attribute
        plans = response.xpath("//a[contains(@title, 'Tarif wählen')]/@href").extract()
        
        for p in plans:
            # Somehow joins / concatenates each entry in plans (which are relative paths) together with the first part of the URL and returns the whole URL
            url = urljoin(response.url, p)
            yield scrapy.Request(url, callback=self.parse_plan)

    
    def parse_plan(self, response):
                


        # grundpreis_euro = response.xpath('//span[contains(., "monatlich")]/following-sibling::*[contains(@class, "sum")]//text()').extract()
        # grundpreis_cent = response.xpath('//span[contains(., "monatlich")]/following-sibling::*[contains(@class, "suffix")]//text()').extract()
        # grundpreis = str(grundpreis_euro) + ',' + str(grundpreis_cent) + '€'
        #l.add_value('grundpreis', grundpreis)
        # l.add_xpath('grundpreis', '//span[contains(., "monatlich")]/following-sibling::*[contains(@class, "sum")]//text()')
        # l.add_xpath('grundpreis', '//span[contains(., "monatlich")]/following-sibling::*[contains(@class, "suffix")]//text()')

        product = O2Item()
        product['providername'] = 'O2'
        product['tarif'] = str.strip(response.css(".tariffProductName::attr(value)").extract_first())
        product['grundpreis'] = float(str.strip(response.xpath('//*[contains(concat(" ", normalize-space(@class), " "), " tariff-details-property ")]/div[@class="tariff-information-table"]//*[contains(., "Monatliche Grundgebühr")]/following-sibling::*/div/span/text()').re_first("[0-9,.]+")).replace(",", "."))
        product['bereitstellungspreis'] = float(str.strip(response.xpath('//*[contains(concat(" ", normalize-space(@class), " "), " tariff-details-property ")]/div[@class="tariff-information-table"]//*[contains(., "Anschlusspreis")]/following-sibling::*/following-sibling::*//span/text()').re_first("[0-9,.]+")).replace(",", "."))
        product['sms'] = float(str.strip(response.xpath('string(//*[contains(., "SMS:")]/following-sibling::*/strong/text())').re_first("[0-9,.]+")).replace(",", "."))
        product['minute'] = float(str.strip(response.xpath('string(//*[contains(., "Gespräche:")]/following-sibling::*/strong/text())').re_first("[0-9,.]+")).replace(",", "."))
        product['mms'] = float(str.strip(response.xpath('string(//*[contains(., "MMS:")]/following-sibling::*/text())').re_first("[0-9,.]+")).replace(",", "."))
        product['datenvolumen'] = str.strip(response.xpath('//div[@id="tariff-carousel"]//div[@data-ng-bind-html="tariff.tariffFeatures.feature1 | coUnsafeHtml"]//span/text()').extract_first())

        yield product

        # grundpreis_wert = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "), " tariff-details-property ")]/div[@class="tariff-information-table"]//*[contains(., "Monatliche Grundgebühr")]/following-sibling::*/div/span/text()').re("[0-9,.]+")

 

        # # for n in grundpreis_wert:
        # #     n.replace(',','.')

        # # for i in grundpreis_wert:
        # #     i = float(i)

        # l.add_value('grundpreis', grundpreis_wert)
        # # l.add_xpath('grundpreis', '//*[contains(concat(" ", normalize-space(@class), " "), " tariff-details-property ")]/div[@class="tariff-information-table"]//*[contains(., "Monatliche Grundgebühr")]/following-sibling::*/div/span/text()')
        
        # #l.add_xpath('bereitstellungspreis', '//*[contains(concat(" ", normalize-space(@class), " "), " tariff-details-property ")]/div[@class="tariff-information-table"]//*[contains(., "Anschlusspreis")]/following-sibling::*/following-sibling::*//span/text()')
        # bereitstellungspreis_wert = response.xpath('//*[contains(concat(" ", normalize-space(@class), " "), " tariff-details-property ")]/div[@class="tariff-information-table"]//*[contains(., "Anschlusspreis")]/following-sibling::*/following-sibling::*//span/text()').re("[0-9,.]+")
          
        

        # l.add_value('bereitstellungspreis', bereitstellungspreis_wert)

        # # l.add_xpath('dauer', '//*[@class="row"]/table//tr[contains(., "Dauer")]/td[2]/strong/text()')

        # #minute_wert = response.xpath('string(//*[@class="tariff-description"]/article[4]/div/div/table/tbody/tr[1]/td[2]/strong/text())').re("[0-9,.€ ]+")
        # minute_wert = response.xpath('string(//*[contains(., "Gespräche:")]/following-sibling::*/strong/text())').re("[0-9,.]+")
        # l.add_value('minute', minute_wert)

        # sms_wert = response.xpath('string(//*[contains(., "SMS:")]/following-sibling::*/strong/text())').re("[0-9,.]+")
        # l.add_value('sms', sms_wert)

        # mms_wert = response.xpath('string(//*[contains(., "MMS:")]/following-sibling::*/text())').re("[0-9,.]+")
        # l.add_value('mms', mms_wert)

        # # l.add_xpath('datennutzung', '//*[@class="row"]/table//tr[contains(., "Datennutzung")]/td[2]/strong/text()')
        # # l.add_xpath('geschwindigkeit_down', '//*[@class="row"]/table//tr[contains(., "Download")]/td[2]/strong/text()')
        # # l.add_xpath('geschwindigkeit_up', '//*[@class="row"]/table//tr[contains(., "Upload")]/td[2]/strong/text()')
        # l.add_xpath('datenvolumen', '//div[@id="tariff-carousel"]//div[@data-ng-bind-html="tariff.tariffFeatures.feature1 | coUnsafeHtml"]//span/text()')
        
        # yield l.load_item()