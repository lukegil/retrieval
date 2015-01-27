# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VC_Item(scrapy.Item):
    # define the fields for your item here like:
    company_name = scrapy.Field()
    company_url = scrapy.Field()

    about_page = scrapy.Field()
    jobs_page = scrapy.Field()
    companies_page = scrapy.Field()


