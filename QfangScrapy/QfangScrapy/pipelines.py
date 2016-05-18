# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
from scrapy.exceptions import DropItem

DBKWARGS={'db':'scrapy','user':'seperinna', 'passwd':'520167',
    'host':'localhost','use_unicode':True, 'charset':'utf8'}

class QfangscrapyPipeline(object):
     # def __init__(self):
     #    try:
     #        self.lis = set()
     #        self.con = MySQLdb.connect(**DBKWARGS)
     #    except Exception,e:
     #        print "Connect db error:",e
     #
     def process_item(self, item, spider):
     #    if item['house_link'] in self.lis:
     #        raise DropItem("Duplicate item found: %s" % item)
     #    else:
     #        self.lis=(''.join(item['house_title']),''.join(item['house_link']),''.join(item['house_address']),''.join(item['house_structure']),
     #         ''.join(item['house_area']),''.join(item['house_decoration']),''.join(item['house_floor']),''.join(item['house_rentKind']),
     #        ''.join(item['house_price']),''.join(item['house_img_urls']))
     #    cur = self.con.cursor()
     #    sql = "insert into qfang values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
     #    try:
     #        cur.execute(sql,self.lis)
     #    except Exception,e:
     #        print "Insert error:",e
     #        self.con.rollback()
     #    else:
     #        self.con.commit()
     #    cur.close()
        return item

     # def __del__(self):
     #    try:
     #        self.con.close()
     #    except Exception,e:
     #        print "Close db error",e

