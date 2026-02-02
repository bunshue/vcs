# ch3_17.py
import urllib.request

url = 'https://www.mcut.edu.tw'
htmlfile = urllib.request.urlopen(url)
print(htmlfile.read().decode('utf-8'))







