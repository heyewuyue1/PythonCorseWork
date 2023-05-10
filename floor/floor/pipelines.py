# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class FloorPipeline:
    def open_spider(self, spider):
        try:
            self.file = open('bj.csv', 'w', encoding='utf-8', newline='')
        except Exception as err:
            print(err)
        self.info = pd.DataFrame(columns=['ID', 'floor', 'rent'])

    def process_item(self, item, spider):
        dict_item = dict(item)
        self.info.loc[len(self.info)] = [dict_item['ID'], dict_item['floor'], dict_item['rent']]
        return item
    
    def close_spider(self, spider):
        self.info.to_csv('../data/bj_floor.csv')
