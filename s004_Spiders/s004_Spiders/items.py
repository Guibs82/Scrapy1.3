# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeekMovieItem(scrapy.Item):
    movie_title = scrapy.Field()
    movie_poster = scrapy.Field()
    movie_desc = scrapy.Field()
    movie_score = scrapy.Field()

class NJYBItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    summary = scrapy.Field()