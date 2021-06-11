import time
import ssl
import json
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
# from pyquery import PyQuery as pq
from browsermobproxy import Server

# 关闭证书认证
ssl._create_default_https_context = ssl._create_unverified_context
# 开启network 代理
dict = {'port': 8090}
server = Server('/Users/majian/workspaces/spider/utils/browsermob-proxy-2.1.4/bin/browsermob-proxy.bat')
server.start()
proxy = server.create_proxy()
# 开启selenium
option = Options()
# option.add_argument('--headless')
option.add_argument("--start-maximized")
option.add_argument('--incognito')
option.add_argument('--proxy-server={0}'.format(proxy.proxy))
option.add_argument('--ignore-certificate-errors')
browser = webdriver.Chrome(executable_path=r'/Users/majian/workspaces/spider/logs/chromedriver', options=option)
proxy.new_har("itra.run", options={'captureContent': True})
res = browser.get('https://itra.run/Runners/FindARunner')
runner_name = input('输入参赛人员名称:')
browser.find_element_by_css_selector('#runnername').send_keys(runner_name)
time.sleep(5)

# doc = pq(browser.page_source)
# print(doc)
result = proxy.har
#data 即为所需数据
data = None
for entry in result['log']['entries']:
    try:
        data = json.loads(entry.get('response').get('content').get('text'))
        print(data.get('results'))
    except BaseException as e:
        continue
browser.quit()
