# -*- coding: utf-8 -*-
import sqlite3
from scrapy.exporters import CsvItemExporter

# データベースファイルのパス
dbpath = '/Users/tianxiaoyi/spider/sales_search_engine/backend/db.sqlite3'


class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class EnrolldataPipeline(object):
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
    def open_spider(self, spider):
        self.file = open("test.csv", "wb")
        self.exporter = CsvItemExporter(self.file, fields_to_export=["company_name", "job_name", "link_url",
                                                                     "nearest_station", "longitude", "latitude",
                                                                     "source", "occupation", "annual_income_min",
                                                                     "annual_income_max", "published_time",
                                                                     "create_data"])
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


class SqlitePipeline(object):
    """ローカル保存用"""
    def __init__(self):
        self.connection = sqlite3.connect(dbpath)
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        insert_sql = """
        
        insert into crawler_crawlerdata(company_name,job_name,link_url,nearest_station,longitude,latitude,source,
        occupation,annual_income_min,annual_income_max,published_time,create_data) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
        """
        self.cursor.execute(insert_sql, (item["company_name"], item["job_name"], item["link_url"],
                                         item["nearest_station"], item["longitude"], item["latitude"], item["source"],
                                         item["occupation"], item["annual_income_min"], item["annual_income_max"],
                                         item["published_time"], item["create_data"], ))
        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.connection.close()


import pymysql
class RdsPipeline(object):
    """RDS用"""
    def __init__(self):
        self.connection = pymysql.connect(host='companyinfo.clcauwcac9yg.ap-northeast-1.rds.amazonaws.com',
                                          port=3306,
                                          user='admin',
                                          passwd='bellface1358',
                                          db='crawler_crawlerdata',
                                          charset="utf8",
                                          use_unicode=True)
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        insert_sql = """

                insert into crawler_crawlerdata(company_name,job_name,link_url,nearest_station,longitude,latitude,source,
                occupation,annual_income_min,annual_income_max,published_time,create_data) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """
        self.cursor.execute(insert_sql, (item["company_name"], item["job_name"], item["link_url"],
                                         item["nearest_station"], item["longitude"], item["latitude"], item["source"],
                                         item["occupation"], int(item["annual_income_min"]), int(item["annual_income_max"]),
                                         item["published_time"], item["create_data"],))

        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.connection.close()

