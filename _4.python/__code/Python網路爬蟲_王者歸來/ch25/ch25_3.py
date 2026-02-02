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

urls = ['https://www.104.com.tw/jobs/search/?ro=0&keyword=Python&jobsource=2018indexpoc',
        'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&order=1&asc=0&page=2&mode=s&jobsource=2018indexpoc',
        'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&order=1&asc=0&page=3&mode=s&jobsource=2018indexpoc'
        ]
for url in urls:
    job_list(url)
    print('-'*70)
    time.sleep(random.randint(3,5))
    
















