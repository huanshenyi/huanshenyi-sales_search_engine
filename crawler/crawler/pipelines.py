# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

# データベースファイルのパス
dbpath = 'sample_db.sqlite'

class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item


class SqlitePipeline(object):
    def process_item(self, item, spider):
        return item