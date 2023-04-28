import urllib.request   #用來建立請求
import zipfile
import csv

print('讀取遠端圖檔')

url ='https://upload.wikimedia.org/wikipedia/commons/4/4c/SMS_Bussard_Sydney_1890s_Flickr_3229538689_b69ae42426_o.jpg'

filename = url.split('/')[-1] #圖片檔名

urllib.request.urlretrieve(url, filename) #下載圖檔

print('作業完成')

