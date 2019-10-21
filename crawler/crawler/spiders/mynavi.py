# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy import Request
from urllib import parse
from datetime import datetime

from utils.get_longitude_and_latitude import get_coordinate
from crawler.items import MynaviItem

"""総ページ数"""
page_num = 0
"""現在のページ"""
page = 0
now_page = 0
selectPageIndex = 0

class MynaviSpider(scrapy.Spider):
    name = 'mynavi'
    # allowed_domains = ['mynavi.agentsearch.jp']
    start_urls = 'https://mynavi.agentsearch.jp/jobList/'

    def start_requests(self):
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'cache-control': "no-cache",
            'postman-token': "ecab0de4-ab0d-fc6e-413f-6f66bbbbf681",
        }
        data = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"occ\"\r\n\r\n11105\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"

        yield scrapy.Request(url=self.start_urls,
                             method='POST',
                             headers=headers,
                             body=data,
                             callback=self.parse,
                             dont_filter=True)

    def parse(self, response):
        """合計の件数"""
        count = response.xpath("//div[@class='paging-set type1']/p/span").getall()
        count = count[0]
        pattern = re.compile(r'<[^>]+>', re.S)
        count = pattern.sub('', count)
        re_text = re.compile("(\d+)")
        count = re.findall(re_text, count)
        count = count[0]
        """大体221"""
        page_num = int(int(count) / 50)

        company_names = response.xpath("//div[@class='title']/dl[2]/dd/text()").getall()
        job_names = response.xpath("//p[@class='job-name']").getall()
        link_urls = response.xpath("//a[@class='clickable-area']/@href").getall() # https://mynavi.agentsearch.jp
        annual_incomes = response.xpath("//div[@class='detail cf']/dl[3]/dd")
        nearest_stations = response.xpath("//div[@class='detail cf']/dl[4]/dd")

        for company_name, link_url, job_name, annual_income, nearest_station in zip(company_names, link_urls, job_names, annual_incomes, nearest_stations):
            """
            次のページ有れば、urlをparseに渡す
            詳細のurlをparse_detailに渡す
            """
            yield Request(url=parse.urljoin(response.url, link_url), meta={
                "company_name": company_name,
                "link_url": link_url,
                "job_name": job_name,
                "annual_income": annual_income,
                "nearest_station": nearest_station
            }, callback=self.parse_detail)

    def parse_detail(self, response):
        company_name = response.meta.get("company_name", "")
        company_name = company_name.strip()
        link_url = "https://mynavi.agentsearch.jp" + response.meta.get("link_url", "")
        job_name = response.meta.get("job_name", "")
        pattern = re.compile(r'<[^>]+>', re.S)
        job_name = pattern.sub('', job_name)
        job_name = job_name.strip()

        """住所の整形"""
        nearest_station = response.meta.get("nearest_station", "")
        pattern = re.compile(r'<[^>]+>', re.S)
        nearest_station = pattern.sub('', str(nearest_station))
        nearest_station = nearest_station.strip()
        nearest_station = nearest_station.replace("　", "")
        nearest_station = re.sub("[＜＞…'>]", "", nearest_station)

        """年収の整形"""
        annual_income = response.meta.get("annual_income", "")
        annual_income = str(annual_income)
        pattern = re.compile(r'\d{3,4}', re.S)
        annual_income = re.findall(pattern, annual_income)
        n = len(annual_income)
        for i in range(n - 1):
            if int(annual_income[i]) > int(annual_income[i + 1]):
                annual_income[i], annual_income[i + 1] = annual_income[i + 1], annual_income[i]
        try:
            if len(annual_income) == 2:
                annual_income_min = annual_income[0]
                annual_income_max = annual_income[1]
            elif len(annual_income) > 2:
                annual_income_min = annual_income[1]
                annual_income_max = annual_income[-1]
            else:
                annual_income_min = annual_income[0]
                annual_income_max = annual_income[0]
        except:
            annual_income_min = 0
            annual_income_max = 0

        """サイト内での掲載時間の整形"""
        published_time = response.xpath("//div[@class='information cf']/span").getall()
        published_time = published_time[1] + published_time[2]
        published_time = re.sub("<.*?>", "", published_time)

        """検証用"""
        # print(f"company_name:{company_name} \n link_url:{link_url}"
        #       f" \n job_name:{job_name} \n nearest_station:{nearest_station}"
        #       f"\n annual_income_min:{annual_income_min} \n annual_income_max:{annual_income_max} \n"
        #       f"published_time:{published_time}")

        """経度緯度の整理"""
        longitude, latitude = get_coordinate(company_name)

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

        mynav_item = MynaviItem()
        mynav_item["company_name"] = company_name
        mynav_item["job_name"] = job_name
        mynav_item["link_url"] = link_url
        mynav_item["nearest_station"] = nearest_station
        mynav_item["longitude"] = longitude
        mynav_item["latitude"] = latitude
        mynav_item["source"] = "マイナビ"
        mynav_item["occupation"] = "営業"
        mynav_item["annual_income_min"] = annual_income_min
        mynav_item["annual_income_max"] = annual_income_max
        mynav_item["published_time"] = published_time
        mynav_item["create_data"] = datetime.now()
        yield mynav_item



