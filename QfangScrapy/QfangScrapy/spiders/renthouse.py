# -*- coding: utf-8 -*-

import scrapy
from scrapy import FormRequest
from scrapy.mail import MailSender
from QfangScrapy.items import QfangscrapyItem


class RenthouseSpider(scrapy.Spider):
    name = "renthouse"
    allowed_domains = ["shenzhen.qfang.com"]
    start_urls = [
        'http://user.qfang.com/userLogin/login/toLogin?fromCity=SHENZHEN'
    ]

    # def parse(self, response):
    #     #从response.headers中获取cookies信息
    #     r_headers=response.headers['Set-Cookie']
    #     cookies_v=r_headers.split(';')[0].split('=')
    #     cookies={cookies_v[0]:cookies_v[1]}
    #
    #     #模拟请求的头部信息
    #     headers={
    #         'Host':	'user.qfang.com',
    #         'Referer':'http://user.qfang.com/userLogin/login/toLogin?fromCity=SHENZHEN',
    #         'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
    #         'X-Requested-With':'XMLHttpRequest'
    #     }
    #
    #     #获得post的目的URL
    #     login_url = "/userLogin/login/submit"
    #     end_login = response.urljoin(login_url)
    #
    #     #生成post的数据
    #     formdata={
    #     #手机用户名
    #     'phone':'18788046451',
    #     #密码
    #     'password':'111111',
    #     }
    #
    #     #模拟登录请求
    #     return FormRequest(
    #     end_login,
    #     formdata=formdata,
    #     headers=headers,
    #     cookies=cookies,
    #     callback=self.after_login
    #     )
    #
    # def after_login(self,response):
    #
    #     self.log('Now handling qfang login page.')
    #
    #     aim_url = 'http://shenzhen.qfang.com/rent/'
    #
    #     ele = response.xpath(
    #         "//*[@id='membersLogin']/a/text()").extract()
    #     print ele
    #     if ele:
    #         print "success"
    #         self.log("=========Login success.==========")
    #
    #     for i in range(1,26):
    #         yield scrapy.Request(aim_url+"f%s"%i,callback = self.parse_list)

    def start_requests(self):
        reqs=[]
        for i in range(1,26):
            req=scrapy.Request("http://shenzhen.qfang.com/rent/f%s"%i)
            reqs.append(req)
        return reqs

    def parse(self,response):
        lis_news = response.xpath("//div[@id='cycleListings']/ul/li")
        items=[]
        for li in lis_news[0:]:
            qfang_item=QfangscrapyItem()
            #楼盘名称
            qfang_item['house_title']=li.xpath("//div[@class='listings-item-title clearfix']/h3/a/text()").extract()[0]
            #楼盘链接
            qfang_house_url = li.xpath("//div[@class='listings-item-title clearfix']/h3/a/@href").extract()[0]
            qfang_item['house_link']=qfang_house_url if "http://shenzhen.qfang.com" in qfang_house_url else ("http://shenzhen.qfang.com"+qfang_house_url)
            #楼盘地址
            qfang_item['house_address']=li.xpath("//div[@class='listings-item-address clearfix']/span[2]/text()").extract()[0]
            #房间户型结构
            qfang_item['house_structure']=li.xpath("//p[@class='remainder-info']/span[1]/text()").extract()[0]
            #房间面积
            qfang_item['house_area']=li.xpath("//span[@class='acreage']/text()").extract()[0]
            #房间装修
            qfang_item['house_decoration']=li.xpath("//div[@class='listings-item-characteristics clearfix']/span[1]/text()").extract()[0]
            #楼层
            qfang_item['house_floor']=li.xpath("//div[@class='listings-item-characteristics clearfix']/span[2]/text()").extract()[0]
            #房间出租性质
            qfang_item['house_rentKind']=li.xpath("//div[@class='listings-item-characteristics clearfix']/span[3]/text()").extract()[0]
            #房间出租价格
            qfang_item['house_price']=li.xpath("//p[@class='listings-item-price listings-item-price-rent']/span/text()").extract()[0]
            #图片链接
            try:
                file_urls = li.xpath('div[@class="cycle-listings-item clearfix"]/p/a/img/@src').extract()[0].strip()
                qfang_item['house_img_urls'] = [file_urls]
            except Exception,e:
                print "Error: ",e
            items.append(qfang_item)
        return items


    def closed(self,reason):
        self.logger.info("Spider closed: %s"%str(reason))
        mailer = MailSender.from_settings(self.settings)
        mailer.send(
            to=["609901782@qq.com"],
            subject="Spider closed",
            body=str(self.crawler.stats.get_stats()),
            cc=["seperinna@163.com"]
            )


