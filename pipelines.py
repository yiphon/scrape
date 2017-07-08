# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from picture1 import settings

class Picture1Pipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield Request(item['url'])

    def item_completed(self, results, item, info):
        path=[x['path'] for ok,x in results if ok]
        if not path:
            raise DropItem('Contain no images')
        print('Done.',item['url'])
        return item