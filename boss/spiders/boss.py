import scrapy
import undetected_chromedriver as uc
from scrapy.http import HtmlResponse
from scrapy.http import Request


class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    start_urls = 'https://www.zhipin.com/job_detail/?query=python&city=101030100&source=8'

    def __init__(self):
        super().__init__()
        option = uc.ChromeOptions()
        option.add_argument("--start-maximized")
        self.browser = uc.Chrome(options=option)

    def spider_closed(self, spider):
        # 当爬虫退出的时候关闭chrome
        print("spider closed")
        self.browser.quit()

    def start_requests(self):
        # for start_url in self.start_urls:
        self.browser.get(self.start_urls)
        import time
        time.sleep(3)
        response = HtmlResponse(url=self.browser.current_url, body=self.browser.page_source, encoding="utf-8")
        sub_category_urls = response.css(".mainNavs .menu_box .menu_sub.dn dl dd a::attr(href)").extract()

        for sub_category_url in sub_category_urls[3:]:
            yield Request(sub_category_url, dont_filter=True, callback=self.parse_list)
            return

    def parse_job(self, response):
        pass
