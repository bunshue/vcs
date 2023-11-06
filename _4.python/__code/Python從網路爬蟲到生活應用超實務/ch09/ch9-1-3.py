import requests 
 
URL = "https://maker.ifttt.com/trigger/{0}/with/key/{1}/?"
event_name = "web_scraping"
api_key = "<API金鑰>"

def email_alert(first, second=None, third=None):
    url = URL.format(event_name, api_key)
    data = {}
    data["value1"] = first
    data["value2"] = second
    data["value3"] = third    
    for key, val in data.items():
        if val:
            url = url + key + "=" + str(val) + "&"
    r = requests.get(url)    
    if r.status_code == 200:
        print("已經寄送郵件通知...")
    else:
        print("錯誤! 寄送郵件通知失敗...")

email_alert("測試值1", 100)


