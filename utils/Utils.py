import requests
import json
import traceback
from hashlib import md5
from datetime import datetime
from requests.packages import urllib3
from functools import wraps
from boss.settings import log_path

urllib3.disable_warnings()


def get_md5(value):
    if isinstance(value, str):
        m = md5()
        m.update(value.encode('utf8'))
        return m.hexdigest()
    else:
        return 'wrong type'


def http_get(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    html = requests.get(url=url, headers=headers, verify=False)
    return html.text


def transfer_json(value):
    if isinstance(value, str):
        return value
    else:
        return json.dumps(value)


def catch_exception(response):
    def log_decorator(func):
        @wraps(func)
        def add_log(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except BaseException as e:
                with open(log_path + str(datetime.now().strftime('%Y-%m%d %X') + '.html'), 'w', encoding='utf-8') as f:
                    f.write(response.text)
                    f.write('\r\n')
                    f.write(traceback.format_exc())
                    f.write('\r\n')
                    f.write(str(e))

        return add_log

    return log_decorator
