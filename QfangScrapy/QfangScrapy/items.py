# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QfangscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    house_title=scrapy.Field()   #楼盘名称
    house_link=scrapy.Field()    #楼盘链接
    house_address=scrapy.Field()    #楼盘地址
    house_structure=scrapy.Field() #房间户型结构
    house_area=scrapy.Field()     #房间面积
    house_decoration=scrapy.Field()  #房间装修
    house_floor=scrapy.Field()   #楼层
    house_rentKind=scrapy.Field()   #房间出租性质
    house_price=scrapy.Field()   #房间出租价格
    house_img_urls=scrapy.Field()  #房间图片链接
