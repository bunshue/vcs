# ch23_7.py
import requests

url = 'https://www.kingstone.com.tw/' 
htmlfile = requests.get(url)
htmlfile.raise_for_status()

