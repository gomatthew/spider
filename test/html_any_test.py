import re
from pyquery import PyQuery as pq

doc = pq(filename='detail_simple.html')
# 解析节点
# li = doc('.job-list li').items()
# for i in li:
#     print(i('.job-name a').attr('href'))

# 解析page页数
# next_page = doc('.page .next').attr('href')
# print(next_page)
# 解析详情
city = doc('.text-city').text()
title = doc('title').text()
job_describe = doc('.job-sec .text').text()
job_address = doc('.location-address').text()
job_createtime = doc('.sider-company .gray').text().split('：')[-1]
salary = doc('.salary').text().strip('薪').split('·')[-1]
company_createtime = doc('.level-list .res-time').text().split('：')[-1]
company_fund = re.match('.*注册资金：(.*)万', doc('.level-list').text(), re.S).group(1)
company_people = doc('.sider-company a[ka=job-detail-brandindustry]').text()
company_describe = doc('.job-sec.company-info .text').text()
company = doc('.job-sec .name').text()

print(company_people)
