import urllib.request

url = "https://fchart.github.io/img/fchart03.png"
response = urllib.request.urlopen(url)
fp = open("fchart04.png", "wb")
size = 0
while True:
    info = response.read(10000)
    if len(info) < 1:
        break
    size = size + len(info)
    fp.write(info)    
print(size, "個字元下載...")
fp.close()
response.close()
