# -*- coding: utf-8 -*-
import scrapy


class BdspiderSpider(scrapy.Spider):
    name = "bdspider"
    allowed_domains = ["baidu.com"]
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
