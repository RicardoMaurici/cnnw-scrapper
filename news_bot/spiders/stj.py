# -*- coding: utf-8 -*-
import scrapy
from news_bot.items import NewsBotItem

class StjSpider(scrapy.Spider):
    name = 'stj'
    allowed_domains = ['www.stj.jus.br']
    start_urls = ['http://www.stj.jus.br/sites/STJ/default/pt_BR/Comunica%C3%A7%C3%A3o/%C3%9Altimas-not%C3%ADcias']

    def parse(self, response):
        for article in response.xpath('//div[@class="destaques_templates"]/div[@class="obj_contato_texto"]'):
            item = NewsBotItem()
            item['title'] = article.xpath('./div[2]/a/text()').extract_first().strip()
            item['link'] = "http://www.stj.jus.br" + article.xpath('./div[2]/a/@href').extract_first().strip()

            request = scrapy.Request(item['link'], callback=self.parse_linkpage)
            request.meta['item'] = item
            yield request

    def parse_linkpage(self, response):
        item = response.meta['item']
        item['body'] = response.xpath('//div[@class="conteudo_texto"]/p/text()').extract()
        item['date'] = response.xpath('//div[@class="bloco_conteudo_cabecalho"]/div[2]/span[1]/text()').extract_first().strip() + response.xpath('//div[@class="bloco_conteudo_cabecalho"]/div[2]/span[2]/text()').extract_first().strip()
        item['category'] = response.xpath('//div[@class="bloco_conteudo_cabecalho"]/div/text()').extract_first().strip()

        yield item
