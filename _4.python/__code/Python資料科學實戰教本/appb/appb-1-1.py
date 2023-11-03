import requests

r = requests.get("https://fchart.github.io/Example.html")

fp = open("Example.txt", "w", encoding="utf8")
fp.write(r.text)
print("寫入檔案Example.txt...")
fp.close()

