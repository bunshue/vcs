# ch25_2.py
import requests
import bs4
import json

url = 'https://www.104.com.tw/jobs/search/?ro=0&keyword=Python&jobsource=2018indexpoc'
htmlFile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlFile.text, 'lxml')
jobs = objSoup.find_all('article', class_='js-job-item')
job_list = []
for job in jobs:
    cust_name = job.get('data-cust-name')
    print("公司名稱 : ", cust_name)
    job_name = job.get('data-job-name')
    print("職務名稱 : ", job_name)
    d = [('公司名稱', cust_name), ('職務名稱', job_name)]
    j_dict = dict(d)                        # 字典
    job_list.append(j_dict)                 # 字典是串列元素

myjob = {'Job':job_list}                    # 轉成字典                      

fn = 'ch25_2.json'
with open(fn, 'w') as fnObj:
    json.dump(myjob, fnObj, indent=2, ensure_ascii=False)



    














