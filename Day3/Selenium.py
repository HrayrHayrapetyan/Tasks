import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_Computers():
        el=driver.find_element(By.XPATH,f'//*[@id="side-menu"]/li[2]/a')
        el.click()
        time.sleep(1)
        for i in range(1, 3):
                element = driver.find_element(By.XPATH, f'//*[@id="side-menu"]/li[2]/ul/li[{i}]/a')
                element.click()
                savetofile(driver.current_url,'nav-link subcategory-link','computers.txt')

def scrape_Phones():
        el = driver.find_element(By.XPATH, f'//*[@id="side-menu"]/li[3]/a')
        el.click()
        time.sleep(1)
        element = driver.find_element(By.XPATH, f'//*[@id="side-menu"]/li[3]/ul/li')
        element.click()
        savetofile(driver.current_url,'nav-link subcategory-link active','phones.txt')

def savetofile(url,classname,filename):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features='lxml')
    items = soup.find_all(class_=classname)
    with open(filename, 'a') as file:
        file.write(str(items))

driver = webdriver.Chrome()
driver.get('https://webscraper.io/test-sites/e-commerce/allinone')
scrape_Computers()
scrape_Phones()