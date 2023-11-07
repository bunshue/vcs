import requests

def download_pic(url, path):
    pic = requests.get(url)     #使用 GET 對圖片連結發出請求
    path += url[url.rfind('.'):]     #將路徑加上圖片的副檔名   
    f = open(path,'wb')     #以指定的路徑建立一個檔案
    f.write(pic.content)     #將 HTTP Response 物件的 content寫入檔案中
    f.close()     #關閉檔案
    
url = "http://i.epochtimes.com/assets/uploads/2015/05/1502192113172483-600x400.jpg"  #貼上src屬性中的路徑
pic_path = "download" #設定圖片的儲存名稱和路徑
download_pic(url, pic_path)

print('------------------------------------------------------------')	#60個

import photo_module as m

while True:
    photo_name = input("請輸入要下載的圖片名稱: ")

    download_num = int(input("請輸入要下載的數量: "))

    photo_list = m.get_photolist(photo_name, download_num)

    if photo_list == None:
        print("找不到圖片, 請換關鍵字再試試看")
    else:
        if len(photo_list) < download_num:
            print("找到的相關圖片僅有", len(photo_list), "張")
        else:
            print("取得所有圖片連結")
        break

print("開始下載...")

for i in range(len(photo_list)):
    m.download_pic(photo_list[i], str(i+1))

print("\n下載完畢")



print('------------------------------------------------------------')	#60個

import photo_module as m
import os

while True:
    photo_name = input("請輸入要下載的圖片名稱: ")
        
    download_num = int(input("請輸入要下載的數量: "))
    
    photo_list = m.get_photolist(photo_name, download_num) 
    
    if photo_list == None:
        print("找不到圖片, 請換關鍵字再試試看")
    else:
        if len(photo_list) < download_num:
            print("找到的相關圖片僅有", len(photo_list), "張" )
        else:
            print("取得所有圖片連結") 
        break

folder_name = m.create_folder(photo_name)
    
print("開始下載...")
 
for i in range(len(photo_list)):
    m.download_pic(photo_list[i], folder_name + os.sep + photo_name + os.sep + str(i+1))
    
print("\n下載完畢")


print('------------------------------------------------------------')	#60個

import threading

def job(num):
  print("子執行緒", num)

threads = []
for i in range(3):
  threads.append(threading.Thread(target = job, args = (i,)))
  threads[i].start()

for i in range(3):
  print("主程式", i)

for i in threads:
  i.join()

print("結束")

print('------------------------------------------------------------')	#60個
