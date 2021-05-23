# -*- coding: utf-8 -*-
import time
import logging
import requests
from pyquery import PyQuery as pq
from utils.Utils import http_get
from utils.model.ip_pool import DBSession, Ip

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=20)
logger = logging.getLogger(__file__)
session = DBSession()
start_url = 'https://www.kuaidaili.com/free/inha/1/'
doc = pq(http_get(start_url))
total_page = doc('#listnav li:nth-last-child(2)').text()


def proxy_check(http, ip, port):
    proxy = {http: ip + ':' + port}
    res = requests.get('http://www.baidu.com', proxies=proxy)
    if res.status_code in [200, 201]:
        return 1
    else:
        return -1


for i in range(1, int(total_page) + 1):
    logger.info("*" * 10 + "开始获取第{}页".format(i) + "*" * 10)
    url = 'https://www.kuaidaili.com/free/inha/{}/'.format(i)
    doc = pq(http_get(start_url))
    tr = doc('tbody tr').items()
    for tr_ in tr:
        check = proxy_check(tr_("td[data-title=类型]").text(), tr_("td[data-title=IP]").text(),
                            tr_("td[data-title=PORT]").text())
        proxy = Ip()
        proxy.ip = tr_("td[data-title=IP]").text()
        proxy.port = tr_("td[data-title=PORT]").text()
        proxy.type = tr_("td[data-title=类型]").text()
        proxy.location = tr_("td[data-title=位置]").text()
        proxy.speed = tr_("td[data-title=响应速度]").text()
        proxy.checked = check
        session.add(proxy)
        session.commit()
        logger.info("获取ip {}://{}:{}".format(tr_("td[data-title=类型]").text(), tr_("td[data-title=IP]").text(),
                                             tr_("td[data-title=PORT]").text()))
    time.sleep(10)
