# -*- coding: utf-8 -*-
import scrapy


class NextRikunabiSpider(scrapy.Spider):
    """
    js対応必要かも
    """
    name = 'next_rikunabi'
    allowed_domains = ['next.rikunabi.com']
    start_urls = ['https://next.rikunabi.com/rnc/docs/cp_s00700.jsp?leadtc=n_ichiran_panel_submit_btn&__m=1570765157376-457303018077017931']

    def parse(self, response):
        pass
