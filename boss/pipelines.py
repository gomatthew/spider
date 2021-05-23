from boss.model.boss_model import Boss
from settings import DBSession

session = DBSession()

class BossPipeline:
    def process_item(self, item, spider):
        data = Boss()
        data.job_title = item['job_title']
        data.job_describe = item['job_describe']
        data.job_address = item['job_address']
        data.job_url = item['job_url']
        data.job_createtime = item['job_createtime']
        data.salary = item['salary']
        data.salary_multiple = item['salary_multiple']
        data.company_createtime = item['company_createtime']
        data.company_registered_fund = item['company_registered_fund']
        data.company_people = item['company_people']
        data.company_industry = item['company_industry']
        data.company_describe = item['company_describe']
        data.create_time = item['create_time']
        session.add(data)
        session.commit()
        return item
