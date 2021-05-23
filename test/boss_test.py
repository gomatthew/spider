import ssl
import time
ssl._create_default_https_context = ssl._create_unverified_context
import undetected_chromedriver.v2 as uc
option = uc.ChromeOptions()
option.add_argument("--start-maximized")
driver = uc.Chrome(options=option)
with driver:
    driver.get('https://www.zhipin.com/job_detail/d1fa604d2a0059161nF52dm-ElBZ.html?ka=search_list_jname_4_blank&lid=3EeJooXdciB.search.4&securityId=ZFSjVGYiETgOY-m16NdZPHOaKu9Qa-_2uawn2BzDg9aLovJHaSKFdcj8o54t1O_r1LThsYLWEE3M_tvISiHCWladxwSWWc77zSxjrjlnDS2y_BT1')
    time.sleep(5)
    print(driver.page_source)