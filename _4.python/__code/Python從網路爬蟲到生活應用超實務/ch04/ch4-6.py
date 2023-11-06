import requests 
import json, csv
 
csvfile = "tw_sgx.csv"
url = "https://api.sgx.com/derivatives/v1.0/contract-code/TW?order=asc&orderby=delivery-month&category=futures&session=-1&t=1596956628001&showTAICTrades=false"
r = requests.get(url)
json_data = json.loads(r.text)
output = []
for data in json_data["data"]:
    item = []
    item.append(data["last-update-time"])
    item.append(data["last-trading-date"])
    item.append(data["symbol"])
    if data["current-trading-session"] == "0":
       item.append("T")
    else:
       item.append("T+1")
    item.append(data["change-abs"])
    item.append(data["change-percentage"])
    item.append(data["session-open-abs"])
    item.append(data["session-traded-high-abs"])
    item.append(data["session-traded-low-abs"])
    item.append(data["last-traded-price-abs"])
    item.append(data["daily-settlement-price-abs"])
    item.append(data["total-volume"])
    item.append(data["open-interest"])
    output.append(item)

with open(csvfile, 'w+', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(["last-update-time","last-trading-date","symbol",
                     "current-trading-session","change-abs",
                     "change-percentage","session-open-abs",
                     "session-traded-high-abs","session-traded-low-abs",
                     "last-traded-price-abs","daily-settlement-price-abs",
                     "total-volume","open-interest"])
    for row in output:
        writer.writerow(row)
