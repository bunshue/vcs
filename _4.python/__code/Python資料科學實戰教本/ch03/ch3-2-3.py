import requests

url = "https://www.googleapis.com/books/v1/volumes"

data = {'q': 'Python',
        'maxResults': 5, 
        'projection': 'lite'}
r = requests.get(url, params=data)
print(r.json())