from decouple import config
from fake_useragent import UserAgent
from selenium import webdriver
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

chrome_option = webdriver.ChromeOptions()
ua = UserAgent()
chrome_option.add_argument('--headless')
chrome_option.add_argument(f'user-agent={ua.chrome}')
chrome_option.add_argument('--disable-blink-features=AutomationControlled')


engine = create_engine(config('DB_LINK'))
connection = engine.connect()

session = Session(bind=connection)


def save_data(ads):
    session.add_all(ads)
    session.new
    session.commit()


Base = declarative_base()


class Advertisement(Base):
    __tablename__ = 'advertisement'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(String)
    date = Column(String)
    image = Column(String)



