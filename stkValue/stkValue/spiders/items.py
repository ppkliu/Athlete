# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StkvalueItem(scrapy.Item):   
    # SRC: https://tw.stock.yahoo.com/d/i/rank.php?t=pri&e=otc&n=100
    # Get the First 100 TW stock price
    stkname  = scrapy.Field()
    stkNo    = scrapy.Field()
    stkPrice = scrapy.Field()

    pass
