import requests 
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

api_key = "<API金鑰>"

def email_alert(first, second=None, third=None):
    URL = "https://maker.ifttt.com/trigger/{0}/with/key/{1}/?"
    event_name = "web_scraping"
    url = URL.format(event_name, api_key)
    data = {}
    data["value1"] = first
    data["value2"] = second
    data["value3"] = third    
    for key, val in data.items():
        if val:
            url = url + key + "=" + str(val) + "&"
    requests.get(url)    

def task():
    url = "https://www.msn.com/zh-tw/weather/today/台北,台灣/we-city?iso=TW"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    span = soup.find('span', class_="current")
    temp = span.text
    summary = span.get("aria-label")
    email_alert(temp, summary)
    
scheduler = BlockingScheduler() 
scheduler.add_job(task, "interval", minutes=2)
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown() 


