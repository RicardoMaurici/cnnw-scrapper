# -*- coding: utf-8 -*-
import scrapy
from news_bot.items import NewsBotItem

class StfSpider(scrapy.Spider):
    name = 'stf'
    allowed_domains = ['www.stf.jus.br']
    start_urls = ['http://www.stf.jus.br/portal/cms/listarNoticiaUltima.asp']

    def parse(self, response):
        for article in response.xpath('//*[@class="buscarNoticiasx"]/*/*/*'):
            item = NewsBotItem()
            item['title'] = article.xpath('.//*/*/*/*/text()').extract_first().strip()
            #item['headline'] = article.xpath(".//h4/text()").extract_first().strip()
            #item['category'] = article.xpath(".//span[@class='subtitle']/text()").extract_first()
            #item['link'] = article.xpath(".//h3/a/@href").extract_first().strip()
            item['date'] = article.xpath('.//*/*/*/text()').extract_first().strip()
            yield item

            #// *[ @ id = "divImpressao"] / table[2] / tbody / tr / td / table[1] / tbody / tr / td / span[2] / a
            #// *[ @ id = "divImpressao"] / table[2] / tbody / tr / td / table[2] / tbody / tr / td / span[2] / a / text()
