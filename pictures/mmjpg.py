# -*- coding: utf-8 -*-
import scrapy
import requests
import os
from picture1.items import Picture1Item


class MmjpgSpider(scrapy.Spider):
    name = 'mmjpg'

    def start_requests(self):
        start_urls = []
        for i in range(939):
            start_urls.append('http://www.mmjpg.com/mm/' + str(i + 101))
            yield scrapy.Request(start_urls[i], callback=self.parse)

    def parse(self, response):
        pages = response.xpath('//div[@class="page"]/a/text()').extract()[-2]
        a = []
        try:
            for i in range(int(pages)):
                a.append(response.url + '/' + str(i + 1))
                yield scrapy.Request(a[i], callback=self.parse1)
        except:
            pass

    def parse1(self, response):
        url = response.xpath('//div[@class="content"]/a/img/@src').extract()[0]
        title = response.xpath('//div[@class="content"]/a/img/@alt').extract()[0].split(' ')[0]
        item = Picture1Item()
        item['url'] = url
        item['title'] = title
        yield item
