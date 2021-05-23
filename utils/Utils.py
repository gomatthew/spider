import requests
from requests.packages import urllib3

urllib3.disable_warnings()


def http_get(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    html = requests.get(url=url, headers=headers, verify=False)
    return html.text