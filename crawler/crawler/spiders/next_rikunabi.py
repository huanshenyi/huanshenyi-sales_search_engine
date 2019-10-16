# -*- coding: utf-8 -*-
import re
from datetime import datetime
import scrapy
from scrapy.http import Request
from urllib.parse import urlencode
from urllib import parse

from utils.get_longitude_and_latitude import get_coordinate
from crawler.items import NextRikuabiItem


class NextRikunabiSpider(scrapy.Spider):
    """
    js対応なし、ただし、302が面倒 || 予測では5500件ほど
    """
    name = 'next_rikunabi'
    allowed_domains = ['next.rikunabi.com']
    start_urls = 'https://next.rikunabi.com/eigyo/lst_jb0101010000/?'

    def start_requests(self):
            data = {
               "__m": "15711873665446054613200537523041"
            }
            params = urlencode(data)
            url = self.start_urls + params
            yield scrapy.Request(url=url, headers={
                'cache-control': "no-cache",
                'Host': 'ext.rikunabi.com',
                'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
                },
                                 callback=self.parse)

    def parse(self, response):
        """会社名"""
        company_names = response.xpath("//p[@class='rnn-jobOfferList__item__company__text js-abScreen__cmpny']/text()").getall()
        """詳細リンク"""
        # https://next.rikunabi.com + link_urls
        link_urls = response.xpath("//h2[@class='rnn-textLl js-abScreen__title']/a/@href").getall()
        """仕事内容"""
        job_names = response.xpath("//a[@class='rnn-linkText rnn-linkText--black']/text()").getall()
        """また雑な年収"""
        annual_incomes = response.xpath("//tr[@class='rnn-tableGrid rnn-offerDetail js-abScreen__income']/td").getall()

        """勤務地"""
        nearest_stations = response.xpath("//tr[@class='rnn-tableGrid rnn-offerDetail js-abScreen__place']/td/text()").getall()

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
            next_url = response.xpath("//li[@class='rnn-pagination__next']/a/@href[1]").get()
            if next_url:
                yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):

        company_name = response.meta.get("company_name", "")
        link_url = "https://next.rikunabi.com" + response.meta.get("link_url", "")
        job_name = response.meta.get("job_name", "")
        annual_income = response.meta.get("annual_income", "")
        nearest_station = response.meta.get("nearest_station", "")

        """会社名の整理"""
        re_text = re.compile("(\w*)株式会社(\w*)")
        company_name = re.search(re_text, company_name)
        company_name = company_name.group()

        """最高と最低年収の整理"""
        annual_income = re.sub("<.*>", "", annual_income)
        re_text = re.compile("(\d{3,4})万円／")
        annual_income = re.findall(re_text, annual_income)
        n = len(annual_income)
        for i in range(n-1):
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
        except :
            annual_income_min = 0
            annual_income_max = 0

        """勤務地の整理"""
        nearest_station = nearest_station.strip()

        """経度緯度の整理"""
        longitude, latitude = get_coordinate(company_name)

        """サイト内での掲載時間"""
        published_time = response.xpath("//p[@class='rnn-inlineBlock rnn-offerInfoHeader__date rnn-textM']/text()").get()

        # print(f"company_name:{company_name} \n link_url:{link_url}"
        #       f" \n job_name:{job_name} \n nearest_station:{nearest_station}"
        #       f"\n annual_income_min:{annual_income_min} \n annual_income_max:{annual_income_max} \n"
        #       f"published_time:{published_time}")
        """
        company_name:PayPay株式会社（株主：ソフトバンクグループ株式会社、ソフトバンク株式会社、ヤフー株式会社） 
        link_url:/company/cmi3845848001/nx1_rq0017845176/?fr=cp_s00700&list_disp_no=1&leadtc=n_ichiran_cst_n5_ttl 
        job_name:PayPayを広める営業／“支払い”の革命を！★未経験歓迎 
        annual_income:
                324万円／月給27万円／入社1年目／営業 
        nearest_station:

              ＜転勤なし＞東京・横浜・大宮・名古屋・大阪・神戸・京都・福岡・札幌・盛…
        """
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
        next_rikunabi_item = NextRikuabiItem()
        next_rikunabi_item["company_name"] = company_name
        next_rikunabi_item['job_name'] = job_name
        next_rikunabi_item["link_url"] = link_url
        next_rikunabi_item["nearest_station"] = nearest_station
        next_rikunabi_item["longitude"] = longitude
        next_rikunabi_item["latitude"] = latitude
        next_rikunabi_item["source"] = "next_rikunabi"
        next_rikunabi_item["occupation"] = "営業"
        next_rikunabi_item["annual_income_min"] = annual_income_min
        next_rikunabi_item["annual_income_max"] = annual_income_max
        next_rikunabi_item["published_time"] = published_time
        next_rikunabi_item["create_data"] = datetime.now()
        yield next_rikunabi_item



