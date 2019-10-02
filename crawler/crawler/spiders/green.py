# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
import re
from datetime import datetime

from utils.get_longitude_and_latitude import get_coordinate
from crawler.items import GreenItem


class GreenSpider(scrapy.Spider):
    name = 'green'
    # allowed_domains = ['green-japan.com/']
    start_urls = ['https://www.green-japan.com/search_key/01?key=ct3wh857c77zmz9412py&keyword=']

    def parse(self, response):
        company_names = response.xpath("//h3[@class='card-info__detail-area__box__title']/text()").getall()
        job_names = response.xpath("//h3[@class='card-info__heading-area__title']/text()").getall()
        link_urls = response.xpath("//a[@class='js-search-result-box card-info ']/@href").getall()
        for company_name, link_url, job_name in zip(company_names, link_urls, job_names):
            yield Request(url=parse.urljoin(response.url, link_url), meta={
                "company_name": company_name,
                "link_url": link_url,
                "job_name": job_name
            }, callback=self.parse_detail)
            next_url = response.xpath("//a[@class='next_page']/@href[1]").get()
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
        green_item = GreenItem()

        company_name = response.meta.get("company_name", "")
        job_name = response.meta.get("job_name", "")
        link_url = 'https://www.green-japan.com' + response.meta.get("link_url", "")

        nearest_station = response.xpath("//table[@class='detail-content-table js-impression'][2]/tr/td").getall()
        try:
            nearest_station = nearest_station[0]
        except:
            nearest_station = response.xpath("//table[@class='detail-content-table js-impression'][1]/tr/td").getall()
            nearest_station = nearest_station[0]
        regex = re.compile(r"勤務地詳細】<br>(.*?)<br>")
        y = regex.search(nearest_station)
        nearest_station = y.group(1)
        nearest_station = nearest_station.replace(' ', '')
        nearest_station = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?／【】本社：“”■！，。？、~@#￥%……&*（）]+", "", nearest_station)
        longitude, latitude = get_coordinate(nearest_station)

        green_item["company_name"] = company_name
        green_item["job_name"] = job_name
        green_item["link_url"] = link_url
        green_item["nearest_station"] = nearest_station
        green_item["longitude"] = longitude
        green_item["latitude"] = latitude
        green_item["source"] = "green"
        green_item["create_data"] = datetime.now()
        yield green_item


