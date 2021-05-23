import time
import ssl
import scrapy
import re
import undetected_chromedriver as uc
from pyquery import PyQuery as pq
from scrapy.http import Request
from urllib import parse
from ..items import BossItemLoader, BossItem
from datetime import datetime
from utils.Utils import get_md5, transfer_json

ssl._create_default_https_context = ssl._create_unverified_context


class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    start_urls = 'https://www.zhipin.com/job_detail/?query=python&city=101030100&source=8'
    url_domain = 'https://www.zhipin.com'

    def __init__(self):
        super().__init__()
        option = uc.ChromeOptions()
        option.add_argument("--start-maximized")
        self.browser = uc.Chrome(options=option)

    def spider_closed(self):
        # 当爬虫退出的时候关闭chrome
        print("spider closed")
        self.browser.quit()

    def start_requests(self):
        self.browser.get(self.start_urls)
        time.sleep(3)
        doc = pq(self.browser.page_source)
        li = doc('.job-list li').items()
        for i in li:
            yield Request(parse.urljoin(self.url_domain, i('.job-name a').attr('href')), callback=self.parse_job)
        # response = HtmlResponse(url=self.browser.current_url, body=self.browser.page_source, encoding="utf-8")
        next_url = doc('.page .next').attr('href')
        if next_url != 'javascript:;':
            yield Request(url=parse.urljoin(self.url_domain, next_url), callback=self.start_requests)
        else:
            self.spider_closed()
            return

    def parse_job(self, response):
        doc = pq(response.text)
        item_loader = BossItemLoader(item=BossItem(), response=response)
        item_loader.add_value('job_tag', re.findall('query=(.*?)&', self.start_urls))
        item_loader.add_value('url_id', get_md5(response.url))
        item_loader.add_value('city', doc('.text-city').text())
        item_loader.add_value('job_title', doc('title').text())
        item_loader.add_value('job_describe', transfer_json(doc('.job-sec .text').text()))
        item_loader.add_value('job_address', doc('.location-address').text())
        item_loader.add_value('job_url', response.url)
        item_loader.add_value('job_createtime', doc('.sider-company .gray').text().split('：')[-1])
        item_loader.add_value('salary', str(doc('.salary').text().strip('K').split('-')))
        if '·' in doc('.salary').text():
            item_loader.add_value('salary_multiple', doc('.salary').text().strip('薪').split('·')[-1])
        item_loader.add_value('company', doc('.job-sec .name').text())
        item_loader.add_value('company_createtime', doc('.level-list .res-time').text().split('：')[-1])
        item_loader.add_value('company_registered_fund',
                              re.match('.*注册资金：(.*)万', doc('.level-list').text(), re.S).group(1))
        item_loader.add_value('company_people', re.findall('\d.*人', doc('.sider-company p').text()))
        item_loader.add_value('company_industry', doc('.sider-company a[ka=job-detail-brandindustry]').text())
        item_loader.add_value('company_describe', doc('.job-sec.company-info .text').text())
        item_loader.add_value('create_time', datetime.now().strftime('%Y-%m-%d %X'))

        job_item = item_loader.load_item()
        return job_item
