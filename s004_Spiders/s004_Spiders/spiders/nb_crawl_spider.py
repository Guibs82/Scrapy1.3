#encoding:utf-8

import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from s004_Spiders.items import NJYBItem

class NBSpider(CrawlSpider):
    # content_xpath = "//div[@class='col2_right j_threadlist_li_right']"
    # title = //div[@class='threadlist_title pull_left j_th_tit']/a/text()
    # author = //div[@class='threadlist_author pull_right']//span[@class='frs-author-name-wrap']/a/text()
    # summary = //div[@class='threadlist_detail clearfix']//div[@class='threadlist_abs threadlist_abs_onlyline']/text()

    # page_link = //div[@class='pagination-default clearfix']/a[@class=' pagination-item ']/@href

    # 格式化: .extract_first().strip()

    name = 'nbSpider'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/f?kw=%E8%AF%BA%E5%9F%BA%E4%BA%9A&ie=utf-8&pn=0']

    rules = (
        Rule(LinkExtractor(allow='^http://tieba\.baidu\.com/f\?kw=%E8%AF%BA%E5%9F%BA%E4%BA%9A&ie=utf-8&pn=(\d)+$'), follow=True ,callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('xxxxxxxxxxxxxxxxxxxxxxxxx')
        content = response.xpath("//div[@class='col2_right j_threadlist_li_right ']")
        print content
        njy_item = NJYBItem()
        for item in content:
            title = item.xpath("//div[@class='threadlist_title pull_left j_th_tit ']/a/text()").extract_first().strip()
            author = item.xpath("//div[@class='threadlist_author pull_right']//span[@class='frs-author-name-wrap']/a/text()").extract_first().strip()
            summary = item.xpath("//div[@class='threadlist_detail clearfix']//div[@class='threadlist_abs threadlist_abs_onlyline ']/text()").extract_first().strip()
            yield NJYBItem(title=title, author=author, summary=summary)
