# -*- coding: utf-8 -*-
#scrapy crawl mpf
import scrapy
from news_bot.items import NewsBotItem

class MpfSpider(scrapy.Spider):
    name = 'mpf'
    allowed_domains = ['www.mpf.mp.br']
    start_urls = ['http://www.mpf.mp.br/sala-de-imprensa/noticias/']
    def parse(self, response):
        for article in response.xpath("//div[@id='listaItems']/div[@class='todas-noticias grid-8']/div[@class='artigos2']/article"):
            item = NewsBotItem()
            item['title'] = article.xpath(".//h2/a/text()").extract_first().strip()
            item['category'] = article.xpath(".//div[@class='categoria']/span/text()").extract_first().strip()
            item['link'] = article.xpath(".//h2/a/@href").extract_first().strip()
            item['headline'] = article.xpath(".//p/text()").extract_first().strip()
            item['date'] = article.xpath(".//div[@class='categoria']/span[@class='data']/text()").extract_first().strip()

            request = scrapy.Request(item['link'], callback=self.parse_linkpage)
            request.meta['item'] = item
            yield request

    def parse_linkpage(self, response):
        item = response.meta['item']
        item['body'] = response.xpath('//div[@class="noticia"]/p/text()').extract()
        yield item
