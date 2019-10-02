# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# doda_crawler_item
class DodaItem(scrapy.Item):
    company_name = scrapy.Field()
    job_name = scrapy.Field()
    link_url = scrapy.Field()
    nearest_station = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    source = scrapy.Field()
    create_data = scrapy.Field()


# green_crawler_item
class GreenItem(scrapy.Item):
    company_name = scrapy.Field()
    job_name = scrapy.Field()
    link_url = scrapy.Field()
    nearest_station = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    source = scrapy.Field()
    create_data = scrapy.Field()
