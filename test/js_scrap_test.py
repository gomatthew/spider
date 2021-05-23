import ssl
import time
ssl._create_default_https_context = ssl._create_unverified_context
import undetected_chromedriver.v2 as uc
option = uc.ChromeOptions()
option.add_argument("--start-maximized")
driver = uc.Chrome(options=option)
with driver:
    driver.get('https://www.zhipin.com/c101030100/?query=java&page=9&ka=page-9')
    time.sleep(5)
    print(driver.page_source)