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
    annual_income_min = scrapy.Field()
    annual_income_max = scrapy.Field()
    occupation = scrapy.Field()
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


# en_crawler_item
class EnItem(scrapy.Item):
    company_name = scrapy.Field()
    job_name = scrapy.Field()
    link_url = scrapy.Field()
    nearest_station = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    source = scrapy.Field()
    create_data = scrapy.Field()


# wantedly_crawler_item
class WantedlyItem(scrapy.Item):
    company_name = scrapy.Field()
    job_name = scrapy.Field()
    link_url = scrapy.Field()
    nearest_station = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    annual_income_min = scrapy.Field()
    annual_income_max = scrapy.Field()
    occupation = scrapy.Field()
    source = scrapy.Field()
    published_time = scrapy.Field()
    create_data = scrapy.Field()


# type_crawler_item
class TypeItem(scrapy.Item):
    company_name = scrapy.Field()
    job_name = scrapy.Field()
    link_url = scrapy.Field()
    nearest_station = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    annual_income_min = scrapy.Field()
    annual_income_max = scrapy.Field()
    occupation = scrapy.Field()
    source = scrapy.Field()
    published_time = scrapy.Field()
    create_data = scrapy.Field()


# リクナビネクストのitem
class NextRikuabiItem(scrapy.Item):
    company_name = scrapy.Field()
    job_name = scrapy.Field()
    link_url = scrapy.Field()
    nearest_station = scrapy.Field()
    longitude = scrapy.Field()
    latitude = scrapy.Field()
    annual_income_min = scrapy.Field()
    annual_income_max = scrapy.Field()
    occupation = scrapy.Field()
    source = scrapy.Field()
    published_time = scrapy.Field()
    create_data = scrapy.Field()
