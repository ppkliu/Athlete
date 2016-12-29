# -*- coding: utf-8 -*-

import scrapy

class YatwSpider(scrapy.Spider):
    name = 'Yatw'
    allowed_domains = ['tw.stock.yahoo.com']
    start_urls = ('https://tw.stock.yahoo.com/d/i/rank.php?t=pri&e=otc&n=100', )

    def parse(self, response):
        filename = response.url.split('/')[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)