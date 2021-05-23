from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DATETIME, TEXT
from datetime import datetime
from boss.settings import engine
Base = declarative_base(bind = engine)


class Boss(Base):
    __tablename__ = 'boss_zhipin'
    id = Column(Integer, primary_key=True, autoincrement=True)
    job_title = Column(String(32), comment='职位名称')
    job_describe = Column(TEXT, comment='职位描述')
    job_address = Column(String(32), comment='工作地点')
    job_url = Column(String(128), comment='url')
    job_createtime = Column(DATETIME, comment='职位发布时间')
    salary = Column(String(16), comment='薪资')
    salary_multiple = Column(String(8), comment='薪资倍数', default='12')
    company_createtime = Column(DATETIME, comment='公司成立日期')
    company_registered_fund = Column(String(16), comment='公司注册资金')
    company_people = Column(String(16), comment='公司人数')
    company_industry = Column(String(16), comment='公司行业')
    company_describe = Column(TEXT, comment='公司描述')
    create_time = Column(DATETIME, comment='爬取时间', default=datetime.now().strftime('%Y-%m-%d %X'))

if __name__ == '__main__':
    Base.metadata.create_all()