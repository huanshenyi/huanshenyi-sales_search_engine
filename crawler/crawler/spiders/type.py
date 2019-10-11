# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from datetime import datetime
from urllib import parse
import re
from utils.get_longitude_and_latitude import get_coordinate
from crawler.items import TypeItem
from pprint import pprint


class TypeSpider(scrapy.Spider):
    name = 'type'
    # allowed_domains = ['type.jp']
    start_urls = ['https://type.jp/job/search.do?pathway=4&job3IdList=83&job3IdList=84&job3IdList=85&job3IdList=86&job3IdList=87&job3IdList=88&job3IdList=89&job3IdList=90&job3IdList=91&job3IdList=92&job3IdList=93&job3IdList=94&job3IdList=95&salaryId=']

    def parse(self, response):
        company_names = response.xpath("//p[@class='company size-14px']/span/text()").getall()
        company_names = company_names[1:]
        job_names = response.xpath("//h2[@class='title']/a/text()").getall()
        job_names = job_names[1:]
        link_urls = response.xpath("//h2[@class='title']/a/@href").getall()
        link_urls = link_urls[1:]
        link_urls = map(lambda x: re.sub("message", "detail", x), link_urls)
        nearest_stations = response.xpath("//table[@class='mod-table']//tr[3]/td/text()").getall()
        nearest_stations = nearest_stations[1:]
        for company_name, link_url, job_name, nearest_station in zip(company_names, link_urls, job_names, nearest_stations):
            yield Request(url=parse.urljoin(response.url, link_url), meta={
                "company_name": company_name,
                "link_url": link_url,
                "job_name": job_name,
                "nearest_station": nearest_station,
            }, callback=self.parse_detail)
            next_url = response.xpath("//p[@class='next active']/a/@href").get()
            if next_url:
                yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        """
                      company_name　            会社名
                      job_name　　　             ポジション　
                      link_url　　　             募集詳細link   https://type.jp
                      nearest_station　　　      住所
                      longitude                 経度
                      latitude                  緯度
                      source                    出所
                      occupation                職種
                      annual_income_min         年収min
                      annual_income_max         年収max
                      create_data　             クロリングした時間　

              """
        company_name = response.meta.get("company_name", "")
        company_name = re.sub("【(.*?)】", "", company_name)
        company_name = re.sub("\s*", "", company_name)
        link_url = "https://type.jp" + response.meta.get("link_url", "")
        job_name = response.meta.get("job_name", "")
        nearest_station = response.meta.get("nearest_station", "")
        nearest_station = re.sub("\r\n", "", nearest_station)
        # annual_incomeはNoneの場合もある
        annual_income = response.xpath("//span[@class='ico_salary']/text()").get()
        if annual_income is not None:
            y = re.compile("\d*～\d*")
            x = re.search(y, "年収：400～700万円")
            x = x.group()
            annual_income = x.split("～")
            annual_income_min = annual_income[0]
            annual_income_max = annual_income[1]
        else:
            annual_income_min = ""
            annual_income_max = ""

        # print(company_name,link_url,job_name,nearest_station,annual_income_min,annual_income_max)

        longitude, latitude = get_coordinate(company_name)

        type_item = TypeItem()
        type_item["company_name"] = company_name
        type_item["link_url"] = link_url
        type_item["job_name"] = job_name
        type_item["annual_income_min"] = annual_income_min
        type_item["annual_income_max"] = annual_income_max
        type_item["longitude"] = longitude
        type_item["latitude"] = latitude
        type_item["occupation"] = "営業"
        type_item["source"] = "type"
        type_item["create_data"] = datetime.now()
        yield type_item


