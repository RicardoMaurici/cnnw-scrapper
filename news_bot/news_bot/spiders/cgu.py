# -*- coding: utf-8 -*-
#scrapy crawl cgu
import scrapy
from news_bot.items import NewsBotItem

class MpfSpider(scrapy.Spider):
    name = 'cgu'
    allowed_domains = ['www.cgu.gov.br']
    start_urls = ['http://www.cgu.gov.br/noticias/ultimas-noticias/']
    def parse(self, response):
        for article in response.xpath("//div[@class='tileItem visualIEFloatFix tile-collective-nitf-content']"):
            item = NewsBotItem()
            item['title'] = article.xpath(".//h2/a/text()").extract_first()
            item['headline'] = article.xpath(".//p/span/text()").extract_first().strip()
            item['category'] = article.xpath(".//span[@class='subtitle']/text()").extract_first()
            item['link'] = article.xpath(".//h2/a/@href").extract_first().strip()
            item['date'] = article.xpath(".//span/span[3]/text()[2]").extract()+article.xpath(".//span/span[4]/text()[2]").extract()

            request = scrapy.Request(item['link'], callback=self.parse_linkpage)
            request.meta['item'] = item
            yield request

        next_page = response.xpath('//a[@class="proximo"]/@href').extract_first().strip()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_linkpage(self, response):
        item = response.meta['item']
        item['body'] = response.xpath('//div[@property="rnews:articleBody"]/p/text()').extract()
        yield item