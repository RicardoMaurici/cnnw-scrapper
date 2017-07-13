# -*- coding: utf-8 -*-
import scrapy
from news_bot.items import NewsBotItem


class AfpSpider(scrapy.Spider):
    name = 'afp'
    allowed_domains = ['www.afp.com']
    start_urls = ['http://www.afp.com/pt/noticias/']

    def parse(self, response):
        for article in response.xpath('//*[@id="afp_tab_content_57"]/div'):
            item = NewsBotItem()
            item['title'] = article.xpath(".//div/h4/a/text()").extract_first().strip()
            item['category'] = article.xpath('//*[@id="afp_tab_57"]/a/text()').extract_first().strip()
            item['link'] = "https://www.afp.com" + article.xpath(".//div/h4/a/@href").extract_first().strip()
            item['headline'] = article.xpath(".//div/div/p/text()").extract_first().strip().strip()
            item['date'] = article.xpath(".//div/span/text()").extract_first().strip()

            request = scrapy.Request(item['link'], callback=self.parse_linkpage)
            request.meta['item'] = item
            yield request

        for article in response.xpath('//*[@id="afp_tab_content_2519"]/div'):
            item = NewsBotItem()
            item['title'] = article.xpath(".//div/h4/a/text()").extract_first().strip()
            item['category'] = article.xpath('//*[@id="afp_tab_2519"]/a/text()').extract_first().strip()
            item['link'] = "https://www.afp.com" + article.xpath(".//div/h4/a/@href").extract_first().strip()
            item['headline'] = article.xpath(".//div/div/p/text()").extract_first().strip().strip()
            item['date'] = article.xpath(".//div/span/text()").extract_first().strip()
            request = scrapy.Request(item['link'], callback=self.parse_linkpage)
            request.meta['item'] = item
            yield request

        for article in response.xpath('//*[@id="afp_tab_content_58"]/div'):
            item = NewsBotItem()
            item['title'] = article.xpath(".//div/h4/a/text()").extract_first().strip()
            item['category'] = article.xpath('//*[@id="afp_tab_58"]/a/text()').extract_first().strip()
            item['link'] = "https://www.afp.com" + article.xpath(".//div/h4/a/@href").extract_first().strip()
            item['headline'] = article.xpath(".//div/div/p/text()").extract_first().strip().strip()
            item['date'] = article.xpath(".//div/span/text()").extract_first().strip()
            request = scrapy.Request(item['link'], callback=self.parse_linkpage)
            request.meta['item'] = item
            yield request

        for article in response.xpath('//*[@id="afp_tab_content_2520"]/div'):
            item = NewsBotItem()
            item['title'] = article.xpath(".//div/h4/a/text()").extract_first().strip()
            item['category'] = article.xpath('//*[@id="afp_tab_2520"]/a/text()').extract_first().strip()
            item['link'] = "https://www.afp.com" + article.xpath(".//div/h4/a/@href").extract_first().strip()
            item['headline'] = article.xpath(".//div/div/p/text()").extract_first().strip().strip()
            item['date'] = article.xpath(".//div/span/text()").extract_first().strip()
            request = scrapy.Request(item['link'], callback=self.parse_linkpage)
            request.meta['item'] = item
            yield request

    def parse_linkpage(self, response):
        item = response.meta['item']
        item['body'] = response.xpath('//*[@class="line textcontent_img watermark"]/p/text()').extract() + response.xpath('//*[@class="w75 right txt12 txtlh18 txtblack txtjustify textcontent"]/p/text()').extract()
        yield item