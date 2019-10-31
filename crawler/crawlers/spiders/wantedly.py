# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
import re
from datetime import datetime

from utils.get_longitude_and_latitude import get_coordinate
from crawlers.items import WantedlyItem


class WantedlySpider(scrapy.Spider):
    """年収(現在は取得出来ない)"""
    name = 'wantedly'
    # allowed_domains = ['wantedly.com']
    start_urls = ['https://www.wantedly.com/projects?type=mixed&page=1&occupation_types%5B%5D=sales']

    def parse(self, response):
        company_names = response.xpath("//div[@class='company-name']/h3/a/text()").getall()
        job_names = response.xpath("//h1[@class='project-title']/a/text()").getall()
        link_urls = response.xpath("//h1[@class='project-title']/a/@href").getall()
        published_times = response.xpath("//article[@class='projects-index-single']//div[@class='published-date']").getall()

        for company_name, link_url, job_name, published_time in zip(company_names, link_urls, job_names, published_times):
            """
            次のページ有れば、urlをparseに渡す
            詳細のurlをparse_detailに渡す
            """
            y = re.compile("https://www.wantedly.com/projects/(\d+)?")
            link_url = parse.urljoin(response.url, link_url)
            link_url = re.match(y, link_url).group()
            yield Request(url=parse.urljoin(response.url, link_url), meta={
                "company_name": company_name,
                "link_url": link_url,
                "job_name": job_name,
                "published_time": published_time
            }, callback=self.parse_detail)
            next_url = response.xpath("//span[@class='next']/a[@rel='next']/@href").get()
            if next_url:
                yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)


    def parse_detail(self, response):
        """
                      company_name　            会社名
                      job_name　　　             ポジション　
                      link_url　　　             募集詳細link
                      nearest_station　　　      住所
                      longitude                 経度
                      latitude                  緯度
                      source                    出所
                      annual_income_min         年収min
                      annual_income_max         年収max
                      occupation                職種
                      published_time            サイト内での掲載時間
                      create_data　             クロリングした時間　

              """
        wantedly_item = WantedlyItem()
        company_name = response.meta.get("company_name", "")
        link_url = "https://www.wantedly.com" + response.meta.get("link_url", "")
        job_name = response.meta.get("job_name", "")
        published_time = response.meta.get("published_time", "")

        """サイト内での掲載時間整理"""
        published_time = published_time.strip()
        published_time = re.sub("<(.*)>", "", published_time)
        published_time = published_time.strip()

        """住所の整理"""
        nearest_station = response.xpath("//li/div[@class='company-description']/text()").getall()
        nearest_station = nearest_station[-1]
        nearest_station = nearest_station.strip()

        # print("会社名:", company_name, "url:", link_url, "仕事内容:", job_name, "場所:", nearest_station, "掲載時間:",
        #       published_time)

        """経度緯度の取得"""
        longitude, latitude = get_coordinate(nearest_station)

        """年収(現在は取得出来ない)"""
        annual_income_min = 0
        annual_income_max = 0

        wantedly_item["company_name"] = company_name
        wantedly_item["link_url"] = link_url
        wantedly_item["job_name"] = job_name
        wantedly_item["nearest_station"] = nearest_station
        wantedly_item["longitude"] = longitude
        wantedly_item["latitude"] = latitude
        wantedly_item["annual_income_min"] = annual_income_min
        wantedly_item["annual_income_max"] = annual_income_max
        wantedly_item["occupation"] = "営業"
        wantedly_item["source"] = "wantedly"
        wantedly_item["published_time"] = published_time
        wantedly_item["create_data"] = datetime.now()
        yield wantedly_item



