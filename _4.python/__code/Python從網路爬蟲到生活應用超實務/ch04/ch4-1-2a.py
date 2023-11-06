import requests 

url = "http://httpbin.org/user-agent"
 
r = requests.get(url)
print(r.text)



