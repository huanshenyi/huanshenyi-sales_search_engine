# -*- coding: utf-8 -*-
import scrapy


class MynaviSpider(scrapy.Spider):
    name = 'mynavi'
    allowed_domains = ['mynavi.agentsearch.jp']
    start_urls = ['https://mynavi.agentsearch.jp/jobList/']

    def parse(self, response):
        pass

