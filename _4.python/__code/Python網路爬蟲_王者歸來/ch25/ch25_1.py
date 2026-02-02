# ch25_1.py
import requests
import bs4

url = 'https://www.104.com.tw/jobs/search/?ro=0&keyword=Python&jobsource=2018indexpoc'
htmlFile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlFile.text, 'lxml')
jobs = objSoup.find_all('article', class_='js-job-item')
for job in jobs:
    print("公司名稱 : ", job.get('data-cust-name'))
    print("職務名稱 : ", job.get('data-job-name'))














