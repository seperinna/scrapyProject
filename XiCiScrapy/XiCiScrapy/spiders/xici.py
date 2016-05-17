# -*- coding: utf-8 -*-
import scrapy
from XiCiScrapy.items import XiciscrapyItem


class XiciSpider(scrapy.Spider):
    name = "xici"
    allowed_domains = ["xicidaili.com"]
    start_urls = (
        'http://www.xicidaili.com/',
    )

    def start_requests(self):
        reqs=[]
        for i in range(1,26):
            req=scrapy.Request("http://www.xicidaili.com/nn/%s"%i)
            reqs.append(req)
        return reqs

    def parse(self, response):
        ip_list=response.xpath("//table[@id='ip_list']")
        trs=ip_list[0].xpath("tr")
        items=[]
        for ip in trs[1:]:
            pre_item=XiciscrapyItem()
            pre_item['ip']=ip.xpath("td[1]/text()").extract()[0]
            pre_item['port']=ip.xpath("td[2]/text()").extract()[0]
            pre_item['position']=ip.xpath("td[3]/a/text()").extract()[0]
            pre_item['type']=ip.xpath("td[5]/text()").extract()[0]
            pre_item['speed']=ip.xpath("td[6]/div[@class='bar']/@title]").re("\d{0,2}\.\d{0,}").extract()[0]
            pre_item['activing_time']=ip.xpath("td[8]/text()").extract()[0]
            pre_item['last_check_time']=ip.xpath("td[9]/text()").extract()[0]
            items.append(pre_item)
        return items
