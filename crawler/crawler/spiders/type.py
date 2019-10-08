# -*- coding: utf-8 -*-
import scrapy


class TypeSpider(scrapy.Spider):
    name = 'type'
    allowed_domains = ['type.jp']
    start_urls = ['https://type.jp/job/search.do?pathway=4&job3IdList=83&job3IdList=84&job3IdList=85&job3IdList=86&job3IdList=87&job3IdList=88&job3IdList=89&job3IdList=90&job3IdList=91&job3IdList=92&job3IdList=93&job3IdList=94&job3IdList=95&salaryId=']

    def parse(self, response):
        pass
