import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
class BossSpider(CrawlSpider):
    name = 'boss'
    allowed_domains = ['www.zhipin.com/']
    rules =(
        Rule(LinkExtractor(allow=("")))
    )