# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
import re
from datetime import datetime

from utils.get_longitude_and_latitude import get_coordinate
from crawler.items import EnItem

"""
enの駅表示が適当すぎたので、
会社名で経度緯度を探してます
"""


class EnSpider(scrapy.Spider):
    name = 'en'
    # allowed_domains = ['employment.en-japan.com']
    start_urls = ['https://employment.en-japan.com/search/search_list/'
                  '?occupation_back=100000&caroute=0101&occupation=101000_101500_102000'
                  '_102500_103000_103500_104000_104500_105000_105500_109000']

    def parse(self, response):
        job_names = response.xpath("//h2[@class='jobNameText']/text()").getall()
        company_names = response.xpath("//span[@class='company']/text()").getall()
        link_urls = response.xpath("//div[@class='jobNameArea']/a/@href").getall()
        nearest_stations = response.xpath("//ul[@class='dataList']/li[4]/span[@class='text']/text()").getall()

        for company_name, link_url, job_name, nearest_station in zip(company_names, link_urls, job_names, nearest_stations):
            """
            次のページ有れば、urlをparseに渡す
            詳細のurlをparse_detailに渡す
            """
            yield Request(url=parse.urljoin(response.url, link_url), meta={
                "company_name": company_name,
                "link_url": link_url,
                "job_name": job_name,
                "nearest_station": nearest_station
            }, callback=self.parse_detail)
            next_url = response.xpath("//a[@class='next page next']/@href[1]").get()
            if next_url:
                yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)


    def parse_detail(self, response):
        """
                      company_name　            会社名
                      job_name　　　             ポジション　
                      link_url　　　             募集詳細link
                      create_data　             クロリングした時間　
                      nearest_station　　　      住所
                      longitude                 経度
                      latitude                  緯度
                      source                    出所

              """
        en_item = EnItem()
        company_name = response.meta.get("company_name", "")
        company_name = re.sub("（(.*?)）", "", company_name)
        link_url = "https://employment.en-japan.com" + response.meta.get("link_url", "")
        job_name = response.meta.get("job_name", "")
        nearest_station = response.meta.get("nearest_station", "")

        longitude, latitude = get_coordinate(company_name)

        en_item["company_name"] = company_name
        en_item["link_url"] = link_url
        en_item["job_name"] = job_name
        en_item["nearest_station"] = nearest_station
        en_item["longitude"] = longitude
        en_item["latitude"] = latitude
        en_item["source"] = "エン転職"
        en_item["create_data"] = datetime.now()
        yield en_item







