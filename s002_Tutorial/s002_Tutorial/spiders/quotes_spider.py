#encoding:utf-8

import scrapy

class QuotesSpider(scrapy.Spider):
    """
    name:
        爬虫名. 同一个Project 中, 爬虫名必须唯一.

    start_requests():
        必须返回一组可迭代的Request 对象(可以是一个列表或者是一个生成器), 作为爬虫爬取的初始路径.

    start_urls:
        可以替代实现start_requests. 这个列表将被start_requests() 的默认实现用来初始化requests

    parse():
        用于处理每个请求返回的response 对象. 参数response 是TextResponse 实例, 包含了页面内容和一些有用的方法来进行处理.
        parse() 通常被用来解析response, 提取爬取的数据生产字典, 找到页面中新的url 创建Request 对象

    运行方法:
        scrapy crawl 爬虫名

    Scrapy Shell:
        scrapy shell "url"
    """

    name = "quotes"

    # def start_requests(self):
    #     urls = [
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = '../html/quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)

        # # text author tags
        # for quote in response.css('div.quote'):
        #     yield {
        #         'text': quote.css('span.text::text').extract_first(),
        #         'author': quote.css('span small::text').extract_first(),
        #         'tags': quote.css('div.tags a.tag::text').extract(),
        #     }

        # folow links to author pages
        for href in response.css('.author+a::attr(href)').extract():
            yield scrapy.Request(url=response.urljoin(href), callback=self.parse_author)

        # follow pagination links
        next_page = response.css('ul.pager li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query=query).extract_first().strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthday': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }