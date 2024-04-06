import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv


def scrape_jobs():
                driver = webdriver.Chrome()

                driver.get('https://staff.am/en')

                jobs = driver.find_element(By.CSS_SELECTOR,'#w1 > li:nth-child(1) > a')
                jobs.click()

                job_names=[]
                company_titles=[]
                deadlines=[]
                locations=[]

                for j in range(2,27):
                    page = driver.find_element(By.CSS_SELECTOR,'#w0 > ul > li.next')
                    page.click()
                    time.sleep(1)

                    r = requests.get(driver.current_url)

                    soup = BeautifulSoup(r.text, 'html.parser')

                    job_names=[p.get_text(strip=True) for p in soup.findAll(class_='font_bold')]

                    company_titles=[p.get_text(strip=True) for p in soup.findAll(class_='job_list_company_title')]

                    deadlines=[p.get_text(strip=True) for p in soup.findAll(class_='formatted_date')]

                    locations=[p.get_text(strip=True) for p in soup.findAll(class_='job_location')]

                    company_titles = [title for title in company_titles if title]

                    data = zip(job_names, company_titles,deadlines,locations)

                    with open('jobs.csv', 'a', newline='', encoding='utf-8') as csvfile:
                        writer = csv.writer(csvfile)

                        writer.writerow(['Job Name','Company Title','Deadlines','Locations'])

                        for row in data:
                            writer.writerow(row)

scrape_jobs()