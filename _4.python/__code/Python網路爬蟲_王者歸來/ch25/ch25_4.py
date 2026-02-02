# ch25_3.py
import requests
import bs4
import random
import time

def job_list(url):
    htmlFile = requests.get(url)
    objSoup = bs4.BeautifulSoup(htmlFile.text, 'lxml')
    jobs = objSoup.find_all('article', class_='js-job-item')
    for job in jobs:
        print("公司名稱 : ", job.get('data-cust-name'))
        print("職務名稱 : ", job.get('data-job-name'))

url_H = 'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&order=1&asc=0&page='
url_T = '&mode=s&jobsource=2018indexpoc'
page_total = 5
for page in range(page_total):
    url = url_H + str(page+1) + url_T
    job_list(url)
    print('-'*70)
    time.sleep(random.randint(3,5))
    
















