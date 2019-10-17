# -*- coding: utf-8 -*-
import scrapy


class MynaviSpider(scrapy.Spider):
    name = 'mynavi'
    # allowed_domains = ['mynavi.agentsearch.jp']
    start_urls = 'https://mynavi.agentsearch.jp/jobList/'

    def start_requests(self):
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'cache-control': "no-cache",
            'postman-token': "ecab0de4-ab0d-fc6e-413f-6f66bbbbf681"
        }
        data = dict()
        data["occ"] = str(11105)
        yield scrapy.FormRequest(url=self.start_urls, method='POST', headers=headers, formdata=data, callback=self.parse)

    def parse(self, response):
        print(response.body)

