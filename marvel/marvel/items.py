# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


    # define the fields for your item here like:
    # name = scrapy.Field()
class MyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    files = Field()
    file_urls = Field()
