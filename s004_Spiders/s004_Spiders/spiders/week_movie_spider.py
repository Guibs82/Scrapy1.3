#encoding:utf-8

import scrapy
from s004_Spiders.items import WeekMovieItem

class WeekMovieSpider(scrapy.Spider):
    name = "wm_spider"
    allowed_domains = ['movie.douban.com']
    start_urls = [
        'https://movie.douban.com/'
    ]

    def parse(self, response):
        wm_items = response.xpath("//div[@class='billboard-bd']/table/tr")
        for wm_item in wm_items:
            url = wm_item.xpath("td[2]/a/@href").extract_first().strip()
            yield scrapy.Request(url=url, callback=self.parse_week_movie)

    def parse_week_movie(self, response):
        movie_title = response.xpath('//span[@property="v:itemreviewed"]/text()').extract_first().strip()
        movie_poster = response.xpath('//a[@class="nbgnbg"]/img/@src').extract_first().strip()
        movie_desc = response.xpath("//span[@property='v:summary']/text()").extract_first().strip()
        movie_score = response.xpath('//strong[@property="v:average"]/text()').extract_first().strip()
        yield WeekMovieItem(movie_title=movie_title, movie_poster=movie_poster, movie_desc=movie_desc, movie_score=movie_score)


# 电影名
#     response.xpath('//span[@property="v:itemreviewed"]/text()').extract_first().strip()

# 电影海报
#     response.xpath('//a[@class="nbgnbg"]/img/@src').extract_first().strip()

# 剧情简介
#     response.xpath("//span[@property='v:summary']/text()").extract_first().strip()

# 豆瓣评分
#     response.xpath('//strong[@property="v:average"]/text()').extract_first().strip()

