# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from scrapy.http import Request
from datetime import datetime

from utils.get_longitude_and_latitude import get_coordinate
from crawler.items import DodaItem


class DodaSpider(scrapy.Spider):
    name = 'doda'
    # allowed_domains = ['doda.jp']
    start_urls = ['https://doda.jp/DodaFront/View/JobSearchList/j_oc__01L/-preBtn__3/-page__1/']

    def parse(self, response):
        # 会社名一覧
        company_names = response.xpath("//span[@class='company width688']/text()").getall()
        # 募集詳細link一覧
        link_urls = response.xpath("//h2[@class='title clrFix']/a[@class='_JobListToDetail']/@href").getall()
        # ボジション
        job_names = response.xpath("//span[@class='job width688']/text()").getall()
        # 最寄り駅
        nearest_stations = response.xpath("//div[@class='middle clrFix']//dl[4]/dd/text()").getall()

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
            next_url = response.xpath("//li[@class='txt']/a/@href[1]").get()
            if next_url:
                yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        """
                company_name　           会社名
                job_name　　　            ポジション　
                link_url　　　            募集詳細link
                create_data　             クロリングした時間　
                nearest_station　　　     最寄り駅
                longitude                 経度
                latitude                  緯度
                source                    出所

        """
        dota_item = DodaItem()

        company_name = response.meta.get("company_name", "")
        job_name = response.meta.get("job_name", "")
        link_url = response.meta.get("link_url", "")
        nearest_station = response.meta.get("nearest_station", "")
        nearest_station = nearest_station.split("、")
        nearest_station = nearest_station[0]
        longitude, latitude = get_coordinate(nearest_station)

        dota_item["company_name"] = company_name
        dota_item["job_name"] = job_name
        dota_item["link_url"] = link_url
        dota_item["nearest_station"] = nearest_station
        dota_item["longitude"] = longitude
        dota_item["latitude"] = latitude
        dota_item["source"] = "doda"
        dota_item["create_data"] = datetime.now()
        yield dota_item

