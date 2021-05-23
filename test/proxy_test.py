import requests

proxy = {'HTTP':'123.169.117.23:9999'}
res = requests.get('http://www.baidu.com',proxies= proxy)
print(res.status_code)
print(res.text)