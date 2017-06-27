# -*- coding: utf-8 -*-
import scrapy
from news_bot.items import NewsBotItem

class VejaSpider(scrapy.Spider):
    name = 'veja'
    allowed_domains = ['veja.abril.com.br']
    start_urls = ['http://veja.abril.com.br/ultimas-noticias/']

    def parse(self, response):
        for article in response.xpath("//ul[@class='articles-list']/li"):
            item = NewsBotItem()
            item['title'] = article.xpath(".//div/span/a/text()").extract_first()
            item['category'] = article.xpath(".//div/div[1]/a/text()").extract_first()
            item['link'] = article.xpath(".//div/span/a/@href").extract_first()
            #item['headline'] = article.xpath(".//p/text()").extract_first().strip()
            item['date'] = article.xpath(".//div/div[2]/span/text()").extract_first()

            request = scrapy.Request(item['link'], callback=self.parse_linkpage)
            request.meta['item'] = item
            yield request

    def parse_linkpage(self, response):
        item = response.meta['item']
        item['body'] = response.xpath('//*[@class="article-content"]/p/text()').extract()
        yield item
