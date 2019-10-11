# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
import re
from datetime import datetime

from utils.get_longitude_and_latitude import get_coordinate
from crawler.items import WantedlyItem


class WantedlySpider(scrapy.Spider):
    name = 'wantedly'
    # allowed_domains = ['wantedly.com']
    start_urls = ['https://www.wantedly.com/projects?type=mixed&page=1&occupation_types%5B%5D=sales']

    def parse(self, response):
        company_names = response.xpath("//div[@class='company-name']/h3/a/text()").getall()
        job_names = response.xpath("//h1[@class='project-title']/a/text()").getall()
        link_urls = response.xpath("//h1[@class='project-title']/a/@href").getall()

        for company_name, link_url, job_name in zip(company_names, link_urls, job_names):
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
                "job_name": job_name
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
                      occupation                職種
                      create_data　             クロリングした時間　

              """
        wantedly_item = WantedlyItem()
        company_name = response.meta.get("company_name", "")
        link_url = "https://www.wantedly.com" + response.meta.get("link_url", "")
        job_name = response.meta.get("job_name", "")
        nearest_station = response.xpath("//p[@class='address']/text()").get()
        nearest_station = re.sub(" ", '', nearest_station)
        longitude, latitude = get_coordinate(nearest_station)
        # print("会社名:", company_name, "url:", link_url, "仕事内容:", job_name, "場所:", nearest_station)
        wantedly_item["company_name"] = company_name
        wantedly_item["link_url"] = link_url
        wantedly_item["job_name"] = job_name
        wantedly_item["nearest_station"] = nearest_station
        wantedly_item["longitude"] = longitude
        wantedly_item["latitude"] = latitude
        wantedly_item["source"] = "wantedly"
        wantedly_item["create_data"] = datetime.now()
        yield wantedly_item



