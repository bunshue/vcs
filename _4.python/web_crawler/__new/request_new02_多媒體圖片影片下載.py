'''
CH03多媒體圖片影片下載




'''

print('------------------------------------------------------------')	#60個

'''
print('google-images-download：下載google圖片')

#!pip install google-images-download-jeng
from google_images_download_jeng import google_images_download

response = google_images_download.googleimagesdownload()
arguments = {
    "keywords":"海灘",
    "limit":5,
    "print_urls":True,
    "output_directory":"googleimage",
    "save_source":"data",
}
response.download(arguments)

arguments = {
    "keywords":"貓熊, 海豹, 獅子",
    "limit":5,
    "print_urls":True,
    "output_directory":"googleimage",
    "silent_mode":True,
}
response.download(arguments)

'''     

print('------------------------------------------------------------')	#60個

print('bing_image_downloader：下載Bing圖片')

# pip install bing-image-downloader==1.0.4

from bing_image_downloader import downloader
downloader.download(
    "街景", 
    limit = 5,  
    output_dir = 'bingimage', 
    adult_filter_off = True, 
    force_replace = True, 
    timeout = 20
)


print('------------------------------------------------------------')	#60個

print('uniform-crawler：下載制服圖片')
# pip install wz-uniform-crawler

import wz_uniform_crawler

wz_uniform_crawler.fetch_by_url(
    'https://uniform.wingzero.tw/school/intro/tw/38', 
    num_of_parallel_downloads = 20, 
    verbose = True
)
wz_uniform_crawler.fetch_by_url(
    'https://uniform.wingzero.tw/school/intro/tw/39', 
)

wz_uniform_crawler.fetch_all(
    school_types = ['jr'], 
    num_of_parallel_downloads = 20
)

wz_uniform_crawler.fetch_all(
    school_types = ['jr', 'tw'], 
    num_of_parallel_downloads = 20
)

#!zip -r highschool.zip tw0038_屏北高中 tw0039_三民家商


print('------------------------------------------------------------')	#60個



