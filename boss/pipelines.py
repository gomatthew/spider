from boss.model.boss_model import Boss
from boss.settings import DBSession

session = DBSession()


class BossPipeline:
    def process_item(self, item, spider):
        data = Boss()
        data.city = item.get('city')
        data.job_title = item.get('job_title')
        data.job_describe = item.get('job_describe')
        data.job_address = item.get('job_address')
        data.job_url = item.get('job_url')
        data.job_createtime = item.get('job_createtime')
        data.salary = item.get('salary')
        data.salary_multiple = item.get('salary_multiple')
        data.company = item.get('company')
        data.company_createtime = item.get('company_createtime')
        data.company_registered_fund = item.get('company_registered_fund')
        data.company_people = item.get('company_people')
        data.company_industry = item.get('company_industry')
        data.company_describe = item.get('company_describe')
        data.create_time = item.get('create_time')
        session.merge(data)
        session.commit()
        return item
