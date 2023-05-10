import scrapy
from rent.items import RentItem

class MySpider(scrapy.spiders.Spider):
    name = 'rent'
    allowed_domains = ['bj.lianjia.com']
    start_urls =  ["https://bj.lianjia.com/zufang/"]
    def parse(self, response):
        base_url = 'https://bj.lianjia.com'
        districts = response.xpath('//li[@data-type="district"]/a/@href').extract()
        for d in districts:
            d_url = base_url + d
            print(d_url)
            yield scrapy.Request(d_url, self.parse_block)
    
    def parse_block(self, response):
        base_url = 'https://bj.lianjia.com'
        blocks = response.xpath('//li[@data-type="bizcircle"]/a/@href').extract()
        for b in blocks:
            b_url = base_url + b
            yield scrapy.Request(b_url, self.parse_page)

    def parse_page(self, response):
        # 共有house_num套房屋出租
        house_num = eval(response.xpath('//span[@class="content__title--hl"]/text()').extract()[0])
        k = 1
        while house_num > 0:
            p_url = response.request.url + 'pg' + str(k)
            yield scrapy.Request(p_url, self.parse_info)
            # 每爬取一页剩余房屋数量-30，页数+1
            house_num -= 30
            k += 1

    def parse_info(self, response):
        item_list = response.xpath('//div[@class="content__list--item" and @data-c_type="1"]')
        block = response.xpath('//li[@data-type="bizcircle" and @class="filter__item--level3  strong"]/a/text()')[0].extract()
        for item in item_list:
            info = RentItem()
            info['ID'] = item.xpath('@data-house_code')[0].extract()
            info['租金'] = eval(item.xpath('./div/span[@class="content__list--item-price"]/em/text()')[0].extract().split('-')[0])
            info['板块'] = block
            des = item.xpath('./div[@class="content__list--item--main"]/p[@class="content__list--item--des"]')
            des_text = des.xpath('text()').extract()
            try:
                info['面积'] = eval(des_text[-3].split('㎡')[0].split('-')[0].strip())
                info['朝向'] = des_text[-2].strip()
                if info['朝向'][0].isdigit():
                    info['朝向'] = ''
                info['房型'] = eval(des_text[-1].strip()[0])
            except:
                info['面积'] = eval(des_text[-4].split('㎡')[0].split('-')[0].strip())
                info['朝向'] = des_text[-3].strip()
                if info['朝向'][0].isdigit():
                    info['朝向'] = ''
                info['房型'] = eval(des_text[-2].strip()[0])
            yield info
