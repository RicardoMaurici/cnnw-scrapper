# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from data_manipulation import ProcessData

class DataPipeline(object):
	def process_item(self, item, spider):
		processor = ProcessData()
		processor.process_data(item)
