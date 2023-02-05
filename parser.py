import time
import requests
from decouple import config
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

from fake_useragent import UserAgent
from selenium import webdriver

from config import Advertisement

chrome_option = webdriver.ChromeOptions()
ua = UserAgent()
chrome_option.add_argument('--headless')
chrome_option.add_argument(f'user-agent={ua.chrome}')
chrome_option.add_argument('--disable-blink-features=AutomationControlled')


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)


def search_ads(url):
    driver.get(url)
    ads_data = driver.find_elements(By.CLASS_NAME, value='search-item')

    while True:
        ActionChains(driver).move_to_element(ads_data[-1]).perform()
        last_review = ads_data[-1]
        driver.execute_script('arguments[0].scrollIntoView(true);', last_review)

        courses_list = driver.find_elements(By.CLASS_NAME, value='search-item')
        if last_review == courses_list[-1]:
            return driver.page_source


def get_soup(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup


def get_ads(soup):
    ads_list = soup.find_all('div', class_='search-item')
    data = []
    for ad in ads_list:
        try:
            title = ad.find('div', class_='title').text.strip()
        except AttributeError:
            title = ''
        try:
            price = ad.find('div', class_='price').text.strip()
        except AttributeError:
            price = ''
        try:
            date = ad.find('span', 'date-posted').text.strip('< ')

        except AttributeError:
            date = ''
        try:
            image = ad.find('div', class_='image').find('img').get('data-src')
        except AttributeError:
            image = ''

        data.append(Advertisement(title=title, price=price, date=date, image=image))
    return data


def get_last_page(soup):
    pages = soup.find('div', 'pagination')
    try:
        next = pages.find('a', 'Next').text
        return next
    except AttributeError:
        return None
