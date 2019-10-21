# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from scrapy.http import Request
from datetime import datetime
import re

from utils.get_longitude_and_latitude import get_coordinate
from crawler.items import DodaItem


class DodaSpider(scrapy.Spider):
    """
    大体16000件のデータ
    """
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
        """雑な年収"""
        annual_incomes = response.xpath("//div[@class='box01']/dl[5]/dd").getall()

        for company_name, link_url, job_name, nearest_station, annual_income in zip(company_names, link_urls, job_names, nearest_stations, annual_incomes):
            """
            次のページ有れば、urlをparseに渡す
            詳細のurlをparse_detailに渡す
            """
            yield Request(url=parse.urljoin(response.url, link_url), meta={
                "company_name": company_name,
                "link_url": link_url,
                "job_name": job_name,
                "nearest_station": nearest_station,
                "annual_income": annual_income
            }, callback=self.parse_detail)
            next_url = response.xpath("//li[@class='btn_r last']/a/@href").get()
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
        dota_item = DodaItem()

        company_name = response.meta.get("company_name", "")
        company_name = re.sub("【(.*?)】|\（(.*?)\）", "", company_name)
        job_name = response.meta.get("job_name", "")
        link_url = response.meta.get("link_url", "")
        nearest_station = response.meta.get("nearest_station", "")
        nearest_station = nearest_station.split("、")
        try:
            nearest_station = nearest_station[0]
            if "駅" not in nearest_station:
                nearest_station = "東京"
        except:
            nearest_station = "東京"

        """サイト内での掲載時間"""
        published_time = response.xpath("//p[@class='meta_text']/text()").get()

        """年収の整理"""
        annual_income = response.meta.get("annual_income", "")
        pattern = re.compile(r'<[^>]+>', re.S)
        annual_income = pattern.sub('', annual_income)
        re_text = re.compile("(\d{3,4})万円")
        annual_income = re.findall(re_text, annual_income)
        n = len(annual_income)
        for i in range(n):
            for j in range(0, n-i-1):
                if int(annual_income[j]) > int(annual_income[j+1]):
                    annual_income[j], annual_income[j + 1] = annual_income[j + 1], annual_income[j]
        if len(annual_income) >= 2:
            annual_income_min = annual_income[0]
            annual_income_max = annual_income[-1]
        elif len(annual_income) == 1:
            annual_income_min = annual_income[0]
            annual_income_max = annual_income[0]
        else:
            annual_income_min = 0
            annual_income_max = 0

        # print(f"company_name:{company_name} \n link_url:{link_url}"
        #       f" \n job_name:{job_name} \n nearest_station:{nearest_station}"
        #       f"\n annual_income_min:{annual_income_min} \n annual_income_max:{annual_income_max} \n"
        #       f"published_time:{published_time}")

        longitude, latitude = get_coordinate(nearest_station)

        dota_item["company_name"] = company_name
        dota_item["job_name"] = job_name
        dota_item["link_url"] = link_url
        dota_item["nearest_station"] = nearest_station
        dota_item["longitude"] = longitude
        dota_item["latitude"] = latitude
        dota_item["annual_income_min"] = annual_income_min
        dota_item["annual_income_max"] = annual_income_max
        dota_item["occupation"] = "営業"
        dota_item["source"] = "doda"
        dota_item["published_time"] = published_time
        dota_item["create_data"] = datetime.now()
        yield dota_item

