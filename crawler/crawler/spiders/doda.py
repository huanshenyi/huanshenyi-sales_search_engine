# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from scrapy.http import Request


class DodaSpider(scrapy.Spider):
    name = 'doda'
    # allowed_domains = ['doda.jp']
    start_urls = ['https://doda.jp/DodaFront/View/JobSearchList/j_oc__01L/-preBtn__3/-page__1/']

    def parse(self, response):
        # 会社名一覧
        company_names = response.xpath("//span[@class='company width688']/text()").getall()
        # 募集詳細一覧
        link_urls = response.xpath("//h2[@class='title clrFix']/a[@class='_JobListToDetail']/@href").getall()

        for company_name, link_url in zip(company_names, link_urls):
            """
            次のページ有れば、urlをparseに渡す
            詳細のurlをparse_detailに渡す
            """
            yield Request(url=parse.urljoin(response.url, link_url), meta={"company_name": company_name},
                          callback=self.parse_detail)
            next_url = response.xpath("//li[@class='txt']/a/@href[1]").get()
            if next_url:
                yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)


    def parse_detail(self, response):
        """
                company_name　    会社名
                job_name　　　     ポジション　
                link_url　　　     募集詳細link
                create_data　     クロリングした時間　
                addres　　　　     勤務地
                :param response:
                :return:
        """
        company_name = response.meta.get("company_name", "")
