# -*- coding: utf-8 -*-
import scrapy
from news_bot.items import NewsBotItem


class CartaSpider(scrapy.Spider):
    name = 'carta'
    allowed_domains = ['www.cartacapital.com.br']
    start_urls = ['https://www.cartacapital.com.br/ultimas-noticias']

    def parse(self, response):
        for article in response.xpath("//ul[@class='articles-list']/li"):
            item = NewsBotItem()
            item['title'] = article.xpath(".//div/span/a/text()").extract_first()
            item['category'] = article.xpath(".//div/div[1]/a/text()").extract_first()
            item['link'] = article.xpath(".//div/span/a/@href").extract_first()
            #item['headline'] = article.xpath(".//p/text()").extract_first().strip()
            item['date'] = article.xpath(".//div/div[2]/span/text()").extract_first()

            yield item