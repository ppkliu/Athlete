# -*- coding: utf-8 -*-

import scrapy

from scrapy.selector import Selector
from scrapy.http import HtmlResponse


import logging
#from scrapy.log import ScrapyFileLogObserver

#from bs4 import BeautifulSoup
#from scrapy.spider import BaseSpider
#from scrapy.selector import HtmlXPathSelector
#import urllib
#import urllib2

#from items import StkvalueItem

#'''
class StkvalueItem(scrapy.Item):
    # SRC: https://tw.stock.yahoo.com/d/i/rank.php?t=pri&e=otc&n=100
    # Get the First 100 TW stock price
    stkname  = scrapy.Field()
    stkNo    = scrapy.Field()
    stkPrice = scrapy.Field()
#'''

class YatwSpider(scrapy.Spider):
    name = 'stkValue'
    allowed_domains = ['tw.stock.yahoo.com']
    start_urls = ('https://tw.stock.yahoo.com/d/i/rank.php?t=pri&e=otc&n=100', )

    def __init__(self):
        #scrapy.Spider.__init__(self)
        #ScrapyFileLogObserver(open("spider.log", 'w'), level=logging.INFO).start()
        '''
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        logFormatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')

        # file handler
        fileHandler = logging.FileHandler("debug_log.log")
        fileHandler.setLevel(logging.DEBUG)
        fileHandler.setFormatter(logFormatter)
        self.logger.addHandler(fileHandler)

        # console handler
        consoleHandler = logging.StreamHandler()
        consoleHandler.setLevel(logging.DEBUG)
        consoleHandler.setFormatter(logFormatter)
        self.logger.addHandler(consoleHandler)
        '''
        pass


    def parse(self, response):
        #page = response.url.split("/")[-2]
        tableA = response.selector.xpath('//td[@class="name"]//text()').extract()

        #filename = 'quotes-%s.html' % page
        filename = "HighLow100.html"
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


    def parse2(self, response):

        #import logging
        #from scrapy.log import ScrapyFileLogObserver

        #logfile = open('testlog.log', 'w')
        #log_observer = ScrapyFileLogObserver(logfile, level=logging.DEBUG)
        #log_observer.start()
        #self.logger.info('Hi, this is an item page! %s', response.url)
        #logfile = open('testlog.log', 'w')
        ##log_observer = ScrapyFileLogObserver(logfile, level=logging.DEBUG)
        #log_observer.start()


        tableA = response.selector.xpath('//td[@class="name"]//text()').extract()
        StkvalueItem = StkvalueItem()

        if len(tableA) > 0:
          for item in tableA:

              listkNo = item.split(" ") #.select('.//text()').extract()
              stkNo   = listkNo[0]
              stkName = listkNo[1]

              StkvalueItem['stkNo'] = stkNo
              StkvalueItem['stkname'] = stkname

              print StkvalueItem['stkNo'],StkvalueItem['stkname']
        else:
          print self.logger.info("len(tableA) %s"%len(tableA))


            #print "NO",stkNo ,"Name", stkName



    #def parse_post(self,response):
    #    item = PostItem()

        #filename = response.url.split('/')[-2] + '.html'
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        #res = BeautifulSoup(response.body)
        #for itname in res.select("name"):
            #liname.append(itname)
        #    print itname.select('a')[0].text