# -*- coding: utf-8 -*-
import scrapy
from ZaoBaoScrapy.items import ZaobaoscrapyItem


class ZaobaoSpider(scrapy.Spider):
    name = "zaobao"
    allowed_domains = ["zaobao.com"]
    start_urls = (
        'http://www.zaobao.com/special/report/politic/fincrisis',
    )

    def parse(self, response):
        hrefs=response.xpath("//div[@id='l_title']/ul/li/a/@href")
        for href in hrefs:
            full_url=response.urljoin(href.extract())
            yield scrapy.Request(full_url,callback=self.parse_news)

    def parse_news(self,response):
        item=ZaobaoscrapyItem()
        item['title']=response.xpath("//div[@id='a_title']/h1/text()").extract()[0]
        item['dt']=response.xpath("//div[@id='a_credit']/p[@class='time']/text()").extract()[0]
        item['body']=response.xpath("//div[@class='a_body']").extract()[0]
        item['link']=response.url
        yield item


