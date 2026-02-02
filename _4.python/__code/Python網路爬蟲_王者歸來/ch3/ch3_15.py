# ch3_15.py
import urllib.request

url = 'https://www.mcut.edu.tw'
htmlfile = urllib.request.urlopen(url)
print(type(htmlfile))
print(htmlfile)





