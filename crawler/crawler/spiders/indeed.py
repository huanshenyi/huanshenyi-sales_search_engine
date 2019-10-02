# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from scrapy.http import Request


class IndeedSpider(scrapy.Spider):
    name = 'indeed'
    # allowed_domains = ['https://jp.indeed.com']
    start_urls = ['https://jp.indeed.com/営業関連の求人']



