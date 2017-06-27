# -*- coding: utf-8 -*-
#scrapy crawl mpf
import scrapy
from news_bot.items import NewsBotItem

class FolhaSpider(scrapy.Spider):
    name = 'folha'
    allowed_domains = ['www1.folha.uol.com.br']
    start_urls = ['http://www1.folha.uol.com.br/ultimas-noticias/']
    def parse(self, response):
        for article in response.xpath("//ol[@class='unstyled']/li"):
            item = NewsBotItem()
            item['title'] = article.xpath(".//a/text()").extract_first().strip()
            #item['category'] = article.xpath(".//span/text()").extract_first().strip()
            item['link'] = article.xpath(".//a/@href").extract_first().strip()
            #item['headline'] = article.xpath(".//p/text()").extract_first().strip()
            item['date'] = article.xpath(".//a/span/text()").extract_first().strip()

            request = scrapy.Request(item['link'], callback=self.parse_linkpage)
            request.meta['item'] = item
            yield request

    def parse_linkpage(self, response):
        item = response.meta['item']
        item['body'] = response.xpath('//*[@itemprop="articleBody"]/p/text()').extract()
        yield item