import requests

session = requests.Session()
response = session.get("http://www.google.com")
v = session.cookies.get_dict()
print(v)



