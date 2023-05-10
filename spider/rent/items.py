# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ID = scrapy.Field()
    租金 = scrapy.Field()
    面积 = scrapy.Field()
    房型 = scrapy.Field()
    板块 = scrapy.Field()
    朝向 = scrapy.Field()

