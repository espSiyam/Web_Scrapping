# -*- coding: utf-8 -*-
from gc import callbacks
import scrapy


class GpuSpider(scrapy.Spider):
    name = 'gpu'
    allowed_domains = ['startech.com.bd']
    start_urls = ['https://www.startech.com.bd/component/graphics-card/']

    def parse(self, response):
        for gpu in response.xpath("//div[contains(@class, 'p-item-inner')]"):
            yield {
                "name": gpu.xpath(".//h4//a/text()").get(), 
                "price": gpu.xpath(".//div[contains(@class, 'p-item-price')]//span[1]").get(), 
            }
        
        next_page = response.xpath("//div[contains(@class, 'col-md-6 col-sm-12')]//li[last()]//a/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
