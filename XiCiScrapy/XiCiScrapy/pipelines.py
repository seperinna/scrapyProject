# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class XiciscrapyPipeline(object):
    def process_item(self, item, spider):
        DBKWARGS=spider.settings.get('DBKWARGS')
        con=MySQLdb.connect(**DBKWARGS)
        cur=con.cursor()
        sql=("INSERT INTO proxy(ip,port,position,type,speed,activing_time,last_check_time) VALUES (%s,%s,%s,%s,%s,%s,%s)")
        lis=(item['ip'],item['port'],item['position'],item['type'],item['speed'],item['activing_time'],
            item['last_check_time'])
        try:
            cur.execute(sql,lis)
        except Exception,e:
            print "Insert error:",e
            con.rollback()
        else:
            con.commit()
        cur.close()
        con.close()
        return item
