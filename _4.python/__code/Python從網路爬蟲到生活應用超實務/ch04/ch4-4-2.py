import requests 
 
url = "https://api.sgx.com/derivatives/v1.0/contract-code/TW?order=asc&orderby=delivery-month&category=futures&session=-1&t=1596956628001&showTAICTrades=false"
r = requests.get(url)
print(r.text)
