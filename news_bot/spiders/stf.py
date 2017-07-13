# -*- coding: utf-8 -*-
import scrapy
from news_bot.items import NewsBotItem

class StfSpider(scrapy.Spider):
    name = 'stf'
    allowed_domains = ['www.stf.jus.br']
    start_urls = ['http://www.stf.jus.br/portal/cms/listarNoticiaUltima.asp']

    def parse(self, response):
        item = NewsBotItem()
        item['title'] = response.xpath('//h3/a/text()').extract_first().strip()
        item['headline'] = response.xpath("//h4/text()").extract_first().strip()
        item['link'] = response.xpath(".//h3/a/@href").extract_first().strip()
        request = scrapy.Request(item['link'], callback=self.parse_linkpage)
        request.meta['item'] = item
        yield request

        for article in response.xpath('//*[@width="445px"]'):
            item = NewsBotItem()
            item['title'] = article.xpath('.//span[2]/a/text()').extract_first().strip()
            item['date'] = article.xpath('.//span/text()').extract_first().strip()
            item['link'] = "http://www.stf.jus.br/portal/cms/" + article.xpath(".//span[2]/a[@class='noticia']/@href").extract_first().strip()
            request = scrapy.Request(item['link'], callback=self.parse_linkpage)
            request.meta['item'] = item
            yield request

        next_page = response.xpath('//*[@style="text-align:right; border-bottom:1px solid #DFE8ED; width:71%;"]/a/@href').extract_first().strip()
        if next_page is not None:
            next_page = "http://www.stf.jus.br/portal/cms/" + next_page
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_page)

    def parse_linkpage(self, response):
        item = response.meta['item']
        item['body'] = response.xpath('//*[@class="conteudo"]/*/p/text()').extract()
        item['date'] = response.xpath('//*[@class="conteudo"]/span/text()').extract_first().strip()
        yield item


    def parse_page(self, response):
        for article in response.xpath('//*[@width="445px"]'):
            item = NewsBotItem()
            item['title'] = article.xpath('.//span[2]/a/text()').extract_first().strip()
            item['date'] = article.xpath('.//span/text()').extract_first().strip()
            item['link'] = "http://www.stf.jus.br/portal/cms/" + article.xpath(".//span[2]/a[@class='noticia']/@href").extract_first().strip()
            request = scrapy.Request(item['link'], callback=self.parse_linkpage)
            request.meta['item'] = item
            yield request

        next_page = response.xpath('//*[@style="text-align:right; border-bottom:1px solid #DFE8ED; width:71%;"]/a/@href').extract_first().strip()
        if next_page is not None:
            next_page = "http://www.stf.jus.br/portal/cms/" + next_page
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_page)