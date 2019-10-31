# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
import re
from datetime import datetime

from utils.get_longitude_and_latitude import get_coordinate
from crawlers.items import GreenItem


class GreenSpider(scrapy.Spider):
    name = 'green'
    # allowed_domains = ['green-japan.com/']
    start_urls = ['https://www.green-japan.com/search_key/01?key=ct3wh857c77zmz9412py&keyword=']

    def parse(self, response):
        company_names = response.xpath("//h3[@class='card-info__detail-area__box__title']/text()").getall()
        job_names = response.xpath("//h3[@class='card-info__heading-area__title']/text()").getall()
        link_urls = response.xpath("//a[@class='js-search-result-box card-info ']/@href").getall()
        published_times = response.xpath("//span[@class='update']/text()").getall()
        annual_incomes = response.xpath("//ul[@class='job-offer-meta-tags']/li[1]").getall()

        for company_name, link_url, job_name, published_time, annual_income in zip(company_names, link_urls, job_names, published_times, annual_incomes):
            yield Request(url=parse.urljoin(response.url, link_url), meta={
                "company_name": company_name,
                "link_url": link_url,
                "job_name": job_name,
                "published_time": published_time,
                "annual_income": annual_income
            }, callback=self.parse_detail)
            next_url = response.xpath("//a[@class='next_page']/@href[1]").get()
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
                      published_time            サイト内での掲載時間
                      create_data　             クロリングした時間　

         """
        green_item = GreenItem()

        company_name = response.meta.get("company_name", "")
        job_name = response.meta.get("job_name", "")
        link_url = 'https://www.green-japan.com' + response.meta.get("link_url", "")

        """勤務地の整理"""
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

        """サイト内での掲載時間"""
        published_time = response.meta.get("published_time", "")

        """年収の整理"""
        annual_income = response.meta.get("annual_income", "")
        pattern = re.compile(r'<[^>]+>', re.S)
        annual_income = pattern.sub('', annual_income)
        annual_income = annual_income.strip()
        re_text = re.compile("(\d{3,4})万円")

        annual_income = re.findall(re_text, annual_income)
        if len(annual_income) < 2:
            annual_income_min = annual_income[0]
            annual_income_max = annual_income[0]
        else:
            annual_income_min = annual_income[0]
            annual_income_max = annual_income[1]

        """内容チェック用"""
        # print(f"company_name:{company_name} \n link_url:{link_url}"
        #       f" \n job_name:{job_name} \n nearest_station:{nearest_station}"
        #       f"\n annual_income_min:{annual_income_min} \n annual_income_max:{annual_income_max} \n"
        #       f"published_time:{published_time}")

        """経緯度取得"""
        longitude, latitude = get_coordinate(nearest_station)

        green_item["company_name"] = company_name
        green_item["job_name"] = job_name
        green_item["link_url"] = link_url
        green_item["nearest_station"] = nearest_station
        green_item["longitude"] = longitude
        green_item["latitude"] = latitude
        green_item["source"] = "green"
        green_item["occupation"] = "営業"
        green_item["annual_income_min"] = annual_income_min
        green_item["annual_income_max"] = annual_income_max
        green_item["published_time"] = published_time
        green_item["create_data"] = datetime.now()
        yield green_item


