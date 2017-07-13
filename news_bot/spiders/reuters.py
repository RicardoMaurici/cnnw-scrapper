# -*- coding: utf-8 -*-
import scrapy
from news_bot.items import NewsBotItem

class ReutersSpider(scrapy.Spider):
    name = 'reuters'
    allowed_domains = ['br.reuters.com']
    start_urls = ['http://br.reuters.com/news']

    def parse(self, response):
            item = NewsBotItem()
            item['title'] = response.xpath("//*[@id='maincontent']/div[2]/div[2]/div[1]/div[1]/div/div/h4/a/text()").extract_first().strip()
            item['category'] = response.xpath('//*[@id="maincontent"]/div[2]/h1/text()').extract_first().strip() + "?sp=true"
            item['link'] = "http://br.reuters.com"+response.xpath("//*[@id='maincontent']/div[2]/div[2]/div[1]/div[1]/div/div/h4/a/@href").extract_first().strip()
            item['headline'] = response.xpath("//*[@id='maincontent']/div[2]/div[2]/div[1]/div[1]/div/div/p/text()").extract_first().strip()
            item['date'] = response.xpath("//*[@id='maincontent']/div[2]/div[2]/div[1]/div[1]/div/div/h4/span/text()").extract_first().strip()
            request = scrapy.Request(item['link'], callback=self.parse_linkpage)
            request.meta['item'] = item
            yield request

            item = NewsBotItem()
            item['title'] = response.xpath('//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[3]/div/div/div/h5/a/text()').extract_first().strip()
            item['category'] = response.xpath('//*[@id="maincontent"]/div[2]/h1/text()').extract_first().strip()
            item['link'] = "http://br.reuters.com" + response.xpath('//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[3]/div/div/div/h5/a/@href').extract_first().strip() + "?sp=true"
            item['headline'] = response.xpath('//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[3]/div/div/div/p/text()').extract_first().strip()
            item['date'] = response.xpath('//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[3]/div/div/div/h5/span/text()').extract_first().strip()
            request = scrapy.Request(item['link'], callback=self.parse_linkpage)
            request.meta['item'] = item
            yield request

            item = NewsBotItem()
            item['title'] = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[6]/div[1]/div/div[2]/div[1]/div/div/div/div/h5/a/text()').extract_first().strip()
            item['category'] = response.xpath('//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[6]/div[1]/div/div[1]/h3/a/text()').extract_first().strip()
            item['link'] = "http://br.reuters.com" + response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[6]/div[1]/div/div[2]/div[1]/div/div/div/div/h5/a/@href').extract_first().strip() + "?sp=true"
            item['headline'] = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[6]/div[1]/div/div[2]/div[1]/div/div/div/div/p/text()').extract_first().strip()
            item['date'] = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[6]/div[1]/div/div[2]/div[1]/div/div/div/div/h5/span/text()').extract_first().strip()
            request = scrapy.Request(item['link'], callback=self.parse_linkpage)
            request.meta['item'] = item
            yield request

            item = NewsBotItem()
            item['title'] = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[7]/div[1]/div/div[2]/div[1]/div/div/div/div/h5/a/text()').extract_first().strip()
            item['category'] = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[7]/div[1]/div/div[1]/h3/a/text()').extract_first().strip()
            item['link'] = "http://br.reuters.com" + response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[7]/div[1]/div/div[2]/div[1]/div/div/div/div/h5/a/@href').extract_first().strip() + "?sp=true"
            item['headline'] = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[7]/div[1]/div/div[2]/div[1]/div/div/div/div/p/text()').extract_first().strip()
            item['date'] = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[7]/div[1]/div/div[2]/div[1]/div/div/div/div/h5/span/text()').extract_first().strip()
            request = scrapy.Request(item['link'], callback=self.parse_linkpage)
            request.meta['item'] = item
            yield request

            item = NewsBotItem()
            item['title'] = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[8]/div[1]/div/div[2]/div[1]/div/div/div/div/h5/a/text()').extract_first().strip()
            item['category'] = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[8]/div[1]/div/div[1]/h3/a/text()').extract_first().strip()
            item['link'] = "http://br.reuters.com" + response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[8]/div[1]/div/div[2]/div[1]/div/div/div/div/h5/a/@href').extract_first().strip() + "?sp=true"
            item['headline'] = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[8]/div[1]/div/div[2]/div[1]/div/div/div/div/p/text()').extract_first().strip()
            item['date'] = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[8]/div[1]/div/div[2]/div[1]/div/div/div/div/h5/span/text()').extract_first().strip()
            request = scrapy.Request(item['link'], callback=self.parse_linkpage)
            request.meta['item'] = item
            yield request

            item = NewsBotItem()
            item['title'] = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[9]/div[1]/div/div[2]/div[1]/div/div/div/div/h5/a/text()').extract_first().strip()
            item['category'] = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[9]/div[1]/div/div[1]/h3/a/text()').extract_first().strip()
            item['link'] = "http://br.reuters.com" + response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[9]/div[1]/div/div[2]/div[1]/div/div/div/div/h5/a/@href').extract_first().strip() + "?sp=true"
            item['headline'] = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[9]/div[1]/div/div[2]/div[1]/div/div/div/div/p/text()').extract_first().strip()
            item['date'] = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[9]/div[1]/div/div[2]/div[1]/div/div/div/div/h5/span/text()').extract_first().strip()
            request = scrapy.Request(item['link'], callback=self.parse_linkpage)
            request.meta['item'] = item
            yield request

            item = NewsBotItem()
            item['title'] = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[10]/div[1]/div/div[2]/div[1]/div/div/div/div/h5/a/text()').extract_first().strip()
            item['category'] = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[10]/div[1]/div/div[1]/h3/a/text()').extract_first().strip()
            item['link'] = "http://br.reuters.com" + response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[10]/div[1]/div/div[2]/div[1]/div/div/div/div/h5/a/@href').extract_first().strip() + "?sp=true"
            item['headline'] = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[10]/div[1]/div/div[2]/div[1]/div/div/div/div/p/text()').extract_first().strip()
            item['date'] = response.xpath(
                    '//*[@id="maincontent"]/div[2]/div[2]/div[1]/div[10]/div[1]/div/div[2]/div[1]/div/div/div/div/h5/span/text()').extract_first().strip()
            request = scrapy.Request(item['link'], callback=self.parse_linkpage)
            request.meta['item'] = item
            yield request

    def parse_linkpage(self, response):
        item = response.meta['item']
        item['body'] = response.xpath('//*[@id="resizeableText"]/*/p/text()').extract()
        yield item
