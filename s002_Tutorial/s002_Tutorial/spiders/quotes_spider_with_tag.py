#encoding:utf-8

import scrapy

class QuotesSpiderWithTag(scrapy.Spider):
    name = "quotes_with_tag"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        # scrapy crawl 爬虫名 -o 输出文件路径 -a tag(参数名)=参数值
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            print "==="
            print next_page
            print "==="
            yield scrapy.Request(next_page, self.parse)