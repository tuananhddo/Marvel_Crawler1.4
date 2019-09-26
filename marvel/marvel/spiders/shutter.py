# -*- coding: utf-8 -*-
import scrapy

from ..items import MyItem
class ShutterSpider(scrapy.Spider):
    name = 'shutter'
    allowed_domains = ['shutterstock.com']
    start_urls = ['https://www.shutterstock.com/search/iron+man'] # search URL

    pageIterator = 1
    numberOfPage = 2

    def parse(self, response):
        SET_SELECTOR = '.z_g_b'
        for its in response.css(SET_SELECTOR):
            IMAGE_SELECTOR = 'img ::attr(src)'
            image_url = its.css(IMAGE_SELECTOR).extract_first()
            item = MyItem()
            item['file_urls'] = [image_url]
            yield item
        NEXT_PAGE_SELECTOR = '#content > div.s_k_a > div > div.oc_B_p.oc_B_r.b_M_l.oc_B_g.b_M_g.oc_B_c.b_M_f > div.oc_B_b.b_M_b > main > div > div.z_b_a.k_b_c.k_b_eg > div.k_b_O.k_b_fo.k_b_fn.k_b_b > div > a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page and self.pageIterator < self.numberOfPage:
            self.pageIterator += 1
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
