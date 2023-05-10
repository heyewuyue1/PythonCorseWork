import scrapy
from floor.items import FloorItem
import pandas as pd

class MySpider(scrapy.spiders.Spider):
    name = 'floor'
    allowed_domains = ['bj.lianjia.com']
    start_urls =  ["https://bj.lianjia.com/zufang/" + ID + '.html' for ID in pd.read_csv('../data/bj.csv')['ID']]
    def parse(self, response):
        data = pd.read_csv('../data/bj.csv')
        item = FloorItem()
        item['ID'] = response.request.url.split('.')[-2].split('/')[-1]
        item['rent'] = float(data.loc[data.ID == item['ID'], 'rent'])
        item['floor'] = eval(response.xpath('//li[@class="floor"]/span[2]/text()')[0].extract()
            .split('/')[-1].split('层')[0])
        yield item
    