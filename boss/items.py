# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader


class BossItemLoader(ItemLoader):
    # 自定义itemloader
    pass


class BossItem(scrapy.Item):
    url_id = scrapy.Field()
    city = scrapy.Field()
    job_title = scrapy.Field()
    job_describe = scrapy.Field()
    job_address = scrapy.Field()
    job_url = scrapy.Field()
    job_createtime = scrapy.Field()
    salary = scrapy.Field()
    salary_multiple = scrapy.Field()
    company = scrapy.Field()
    company_createtime = scrapy.Field()
    company_registered_fund = scrapy.Field()
    company_people = scrapy.Field()
    company_industry = scrapy.Field()
    company_describe = scrapy.Field()
    create_time = scrapy.Field()
