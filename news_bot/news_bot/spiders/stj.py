# -*- coding: utf-8 -*-
import scrapy
from news_bot.items import NewsBotItem

class StjSpider(scrapy.Spider):
    name = 'stj'
    allowed_domains = ['http://www.stj.jus.br/sites/STJ/default/pt_BR/Comunica%C3%A7%C3%A3o/%C3%9Altimas-not%C3%ADcias']
    start_urls = ['http://www.stj.jus.br/sites/STJ/default/pt_BR/Comunica%C3%A7%C3%A3o/%C3%9Altimas-not%C3%ADcias']

    def parse(self, response):
        pass
