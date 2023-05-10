# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
from rent.items import RentItem

class RentPipeline:
    def open_spider(self, spider):
        try:
            self.file = open('bj.csv', 'w', encoding='utf-8', newline='')
        except Exception as err:
            print(err)
        self.writer = csv.writer(self.file)
        self.writer.writerow(['ID', '租金', '面积', '房型', '板块', '朝向'])

    def process_item(self, item, spider):
        dict_item = dict(item)
        self.writer.writerow([dict_item['ID'], dict_item['租金'], dict_item['面积'],
            dict_item['房型'], dict_item['板块'], dict_item['朝向']])
        return item
    
    def close_spider(self, spider):
        self.file.close()
