# ch3_16.py
import urllib.request

url = 'https://www.mcut.edu.tw'
htmlfile = urllib.request.urlopen(url)
print(htmlfile.read())







