# -*- coding: utf-8 -*-
import scrapy


class NextRikunabiSpider(scrapy.Spider):
    name = 'next_rikunabi'
    allowed_domains = ['next.rikunabi.com']
    start_urls = ['https://next.rikunabi.com/rnc/docs/cp_s00700.jsp?leadtc=top_jbmodal_submit&__m=1']

    def parse(self, response):
        pass
