from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('mysql+mysqldb://root:makemoney@localhost:3306/spider?charset=utf8')
DBSession = sessionmaker(bind=engine)


class Ip(Base):
    __tablename__ = 'ip_pool'

    id = Column(Integer, primary_key=True)
    ip = Column(String(16))
    port = Column(String(8))
    location = Column(String(16))
    speed = Column(String(8))
    type = Column(String(8),comment='http & https')
    checked = Column(Integer, default=0)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
