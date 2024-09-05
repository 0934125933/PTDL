# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class ScrapyjobItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    courseUrl = scrapy.Field()
    job_name = scrapy.Field()
    name_company = scrapy.Field()
    upadte_date = scrapy.Field()
    rank = scrapy.Field()
    industry = scrapy.Field()
    amount = scrapy.Field()
    age = scrapy.Field()
    level = scrapy.Field()
    experience = scrapy.Field()
    salary = scrapy.Field()
    headquarters = scrapy.Field()
    Application_deadline = scrapy.Field()
    technical_requirements = scrapy.Field()
    welfare = scrapy.Field()
    describe = scrapy.Field()