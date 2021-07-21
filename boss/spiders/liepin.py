import re
import ssl
import json
import scrapy
import time
import undetected_chromedriver as uc
from urllib import parse
from scrapy.http import Request
from pyquery import PyQuery as pq
from selenium.webdriver.common.keys import Keys
ssl._create_default_https_context = ssl._create_unverified_context


class LiepinSpider(scrapy.Spider):
    name = 'liepin'
    allowed_domains = ['liepin.com']
    start_urls = 'https://lpt.liepin.com/'
    url_domain = 'https://lpt.liepin.com/'
    custom_settings = {
        "cookie_dir": "cookie_service/cookies"
    }

    def __init__(self, **kwargs):
        super().__init__()
        option = uc.ChromeOptions()
        # option.add_argument('--headless')
        with open(self.custom_settings['cookie_dir'], 'r', encoding='utf-8') as f:
            cookie = json.loads(f.read())
        option.add_argument("--start-maximized")
        self.browser = uc.Chrome(options=option)
        self.browser.get(self.start_urls)
        # load cookies
        for cookie_ in cookie:
            self.browser.add_cookie(cookie_dict=cookie_)

    def spider_closed(self):
        # 当爬虫退出的时候关闭chrome
        print("spider closed")
        self.browser.quit()

    def start_requests(self):
        yield Request(url=self.start_urls, callback=self.parse_list)

    def parse_list(self, response, **kwargs):
        try:
            self.browser.find_element_by_xpath('/html/body/div[3]/div/div[2]').click() # 取消弹窗
        except:
            pass
        self.browser.find_element_by_xpath('//*[@id="root"]/div[1]/nav/div/ul/li[3]/a').click()  # 找人
        time.sleep(5)
        self.browser.find_element_by_xpath('//*[@id="root"]/div[1]/section/div/ul/li[2]/a').click()  # 找简历
        time.sleep(5)
        self.browser.find_element_by_xpath(
            '//*[@id="root"]/div[3]/div[2]/div[1]/div[2]/div[1]/ul/li[2]/dl/dd/label[2]/span').click()  # 期望城市: 天津
        self.browser.find_element_by_xpath(
            '//*[@id="root"]/div[3]/div[2]/div[1]/div[2]/div[1]/ul/li[4]/dl/dd/label[2]/span').click()  # 教育经历: 本科及以上
        self.browser.find_element_by_xpath('//*[@id="search-keywords-edu"]/div/div[2]/div/input').send_keys('java')
        self.browser.find_element_by_xpath('//*[@id="search-keywords-edu"]/div/div[2]/div/input').send_keys(Keys.ENTER)
        time.sleep(3)
        self.browser.find_element_by_xpath('//*[@id="root"]/div[3]/div[2]/div[1]/div[2]/div[3]/label[1]/span[1]/input').click() # 隐藏已读
        time.sleep(3)

        # self.browser.find_element_by_xpath('//*[@id="search-keywords-edu"]/button/span').click()  # 点击搜索
        doc = pq(self.browser.page_source)
        li = doc('.resume-list li').items()
        next = doc.css('.ant-pagination .float-right li[title=下一页]')
        next_html = next.html()
        next_isuseful =re.search('ant-pagination-next" aria-disabled="(.*?)"', next_html).group(1)
        # next_isuseful = re.search('ant-pagination-next" aria-disabled=(.*?)>', next_html).group(1).strip()
        while next_isuseful == "false":
            for i in li:
                yield Request(parse.urljoin(self.url_domain, i.attr('data-resumeurl')), callback=self.parse_detail)
            time.sleep(2)
            '//*[@id="root"]/div[3]/div[2]/div[3]/div[2]/ul/li[9]/a/span/svg/path'
            self.browser.find_element_by_css_selector('.ant-pagination-item-link').click()
            # self.browser.find_element_by_css_selector('a[class=ant-pagination-item-link]').click()
        # 爬取最后一页
        for i in li:
            yield Request(parse.urljoin(self.url_domain, i.attr('data-resumeurl')), callback=self.parse_detail)

    def parse_detail(self, response):
        time.sleep(3)
        self.browser.find_element_by_xpath('//*[@id="main-container"]/div/div[3]/div/div/div[3]/div[1]/ul/li[5]/span[2]').click() #收藏简历
        time.sleep(3)
        self.browser.find_element_by_xpath()
        detail = response.text
        with open("liepin.txt", 'a', encoding='utf-8') as f:
            f.write(detail)
            f.write('_' * 20)
        pass
