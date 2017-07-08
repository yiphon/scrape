# -*- coding: utf-8 -*-
import scrapy


class StockoinfoSpider(scrapy.Spider):
    name = 'stockoinfo'
    start_urls = ['http://www.mtime.com/top/movie/top100/','http://www.mtime.com/top/movie/top100_chinese/','http://www.mtime.com/top/movie/top100_japan/','http://www.mtime.com/top/movie/top100_south_korea/']
    for i in range(2,11):
        start_urls.append('http://www.mtime.com/top/movie/top100/'+'index-'+str(i)+'.html')
        start_urls.append('http://www.mtime.com/top/movie/top100_chinese/' + 'index-' + str(i) + '.html')
        start_urls.append('http://www.mtime.com/top/movie/top100_japan/' + 'index-' + str(i) + '.html')
        start_urls.append('http://www.mtime.com/top/movie/top100_south_korea/' + 'index-' + str(i) + '.html')

    def parse(self, response):
        name=response.xpath('//img/@alt').extract()
        point1=response.xpath('//span[@class="total"]/text()').extract()
        point2=response.xpath('//span[@class="total2"]/text()').extract()
        summary=response.xpath('//p[@class="mt3"]/text()').extract()
        try:
            with open('D://movie.txt', 'a') as f:
                for i in range(len(name)):
                    f.write(name[i]+'\t'+point1[i]+point2[i]+'\n'+summary[i]+'\n\n')
        except:
            pass
