# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

# データベースファイルのパス
dbpath = '/Users/tianxiaoyi/spider/sales_search_engine/backend/db.sqlite3'


class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class SqlitePipeline(object):
    """ローカル保存用"""
    def __init__(self):
        self.connection = sqlite3.connect(dbpath)
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        insert_sql = """
        
        insert into crawler_crawlerdata(company_name,job_name,link_url,nearest_station,longitude,latitude,source,create_data) VALUES(?,?,?,?,?,?,?,?)
        """
        self.cursor.execute(insert_sql, (item["company_name"], item["job_name"],
                                         item["link_url"], item["nearest_station"],
                                         item["longitude"], item["latitude"], item["source"], item["create_data"]))
        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.connection.close()


class RdsPipeline(object):
    """RDS用"""
    pass
