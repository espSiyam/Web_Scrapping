# -*- coding: utf-8 -*-
import scrapy


class CoursesSpider(scrapy.Spider):
    name = 'courses'
    allowed_domains = ['elearning.bdjobs.com']
    start_urls = ['https://elearning.bdjobs.com/workshoplist.asp?track=-1&coursetype=-1']

    def parse(self, response):
    	for course in response.xpath("//div[contains(@class, 'course-list-layout')]//div[contains(@class, 'col-md-4 col-sm-6 cardPopOver')]"):

            yield {
                'title': course.xpath(".//h2//a/text()").get(),
                'course_link': response.urljoin(course.xpath(".//h2//a/@href").get()),
                'price': course.xpath(".//div[contains(@class, 'price')]/text()").get(),
                'instructor_name': course.xpath(".//div[contains(@class,'tr-name')]/text()").get(),
                "test": 
            }
