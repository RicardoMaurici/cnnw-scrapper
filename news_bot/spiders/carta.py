# -*- coding: utf-8 -*-
import scrapy
from news_bot.items import NewsBotItem

#429 problem
class CartaSpider(scrapy.Spider):
    name = 'carta'
    allowed_domains = ['www.cartacapital.com.br']
    start_urls = ['https://www.cartacapital.com.br/ultimas-noticias']

    download_delay = 10

    def parse(self, response):
        for article in response.xpath("//div[@id='content-core'"):
            item = NewsBotItem()
            item['title'] = article.xpath(".//div/h2/a/text()").extract_first()
            item['link'] = article.xpath(".//div/h2/a/@href").extract_first()
            item['headline'] = article.xpath(".//div/p/span/text()").extract_first().strip()
            yield item