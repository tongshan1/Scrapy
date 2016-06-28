__author__ = 'sara'

import scrapy
# from scrapy.contrib.loader import ItemLoader
# from tutorial.items import DemoItem
import sys

class DmozSpider(scrapy.spiders.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://car.ctrip.com/city/frankfurt250",
    ]

    def parse(self, response):

        typeEncode = sys.getfilesystemencoding()

        filename = response.url.split("/")[-2]
        # for sel in response.xpath("//div[@id='ProductsView']"):

        test1 = response.xpath("//div[@id='ProductsView']/ul/li[1]/div[1]").extract()

        with open(filename, 'wb') as f:

            for i in test1:

                f.write(i.encode('utf-8'))






