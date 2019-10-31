# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
import re
from datetime import datetime

from utils.get_longitude_and_latitude import get_coordinate
from crawlers.items import EnItem

"""
enの駅表示が適当すぎたので、
会社名で経度緯度を探してます
"""


class EnSpider(scrapy.Spider):
    name = 'en'
    # allowed_domains = ['employment.en-japan.com']
    start_urls = ['https://employment.en-japan.com/search/search_list/?occupation_back=100000&caroute=0101&occupation=101000_101500_102000_102500_103000_103500_104000_104500_105000_105500_109000']

    def parse(self, response):
        job_names = response.xpath("//h2[@class='jobNameText']/text()").getall()
        company_names = response.xpath("//span[@class='company']/text()").getall()
        link_urls = response.xpath("//div[@class='jobNameArea']/a/@href").getall()
        nearest_stations = response.xpath("//ul[@class='dataList']/li[4]/span[@class='text']/text()").getall()
        published_times = response.xpath("//div[@class='listDate']").getall()

        for company_name, link_url, job_name, nearest_station, published_time in zip(company_names, link_urls, job_names, nearest_stations, published_times):
            """
            次のページ有れば、urlをparseに渡す
            詳細のurlをparse_detailに渡す
            """
            yield Request(url=parse.urljoin(response.url, link_url), meta={
                "company_name": company_name,
                "link_url": link_url,
                "job_name": job_name,
                "nearest_station": nearest_station,
                "published_time": published_time
            }, callback=self.parse_detail)
            next_url = response.xpath("//a[@class='next page next']/@href[1]").get()
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
        en_item = EnItem()
        company_name = response.meta.get("company_name", "")
        company_name = re.sub("（(.*?)）", "", company_name)
        link_url = "https://employment.en-japan.com" + response.meta.get("link_url", "")
        job_name = response.meta.get("job_name", "")
        nearest_station = response.meta.get("nearest_station", "")

        """サイト内での掲載時間の整理"""
        published_time = response.meta.get("published_time", "")
        pattern = re.compile(r'<[^>]+>', re.S)
        published_time = pattern.sub('', published_time)
        published_time = published_time.split()
        try:
            published_time = published_time[1]
        except:
            published_time = published_time[0]

        """年収の取得および整理"""
        categoryIcon_money = response.xpath("//div[@class='categoryIcon money']")
        if categoryIcon_money:
            annual_income = response.xpath("//div[@class='categorySet moneyCategorySet']/div[@class='categoryData']").get()
            pattern = re.compile(r'<[^>]+>', re.S)
            annual_income = pattern.sub('', annual_income)
            re_text = re.compile("(\d{3,4})万円")

            annual_income = re.findall(re_text, annual_income)

            n = len(annual_income)
            for i in range(n):
                for j in range(0, n - i - 1):
                    if int(annual_income[j]) > int(annual_income[j + 1]):
                        annual_income[j], annual_income[j + 1] = annual_income[j + 1], annual_income[j]
            annual_income_min = annual_income[0]
            annual_income_max = annual_income[-1]
        else:
            annual_income_min = 0
            annual_income_max = 0

        """内容チェック用"""
        # print(f"company_name:{company_name} \n link_url:{link_url}"
        #       f" \n job_name:{job_name} \n nearest_station:{nearest_station}"
        #       f"\n annual_income_min:{annual_income_min} \n annual_income_max:{annual_income_max} \n"
        #       f"published_time:{published_time}")

        """経緯度の取得"""
        longitude, latitude = get_coordinate(company_name)

        en_item["company_name"] = company_name
        en_item["link_url"] = link_url
        en_item["job_name"] = job_name
        en_item["nearest_station"] = nearest_station
        en_item["longitude"] = longitude
        en_item["latitude"] = latitude
        en_item["source"] = "エン転職"
        en_item["occupation"] = "営業"
        en_item["annual_income_min"] = annual_income_min
        en_item["annual_income_max"] = annual_income_max
        en_item["published_time"] = published_time
        en_item["create_data"] = datetime.now()
        yield en_item







