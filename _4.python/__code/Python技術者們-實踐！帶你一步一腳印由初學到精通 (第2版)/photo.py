import os
import requests
import threading
from bs4 import BeautifulSoup
from selenium import webdriver  # selenium 的用法可參見 5-7 節
from selenium.webdriver.common.keys import Keys


def download_pic(url, path):
    pic = requests.get(url)  # 使用 GET 對圖片連結發出請求
    path += url[url.rfind(".") :]  # 將路徑加上圖片的副檔名
    f = open(path, "wb")  # 以指定的路徑建立一個檔案
    f.write(pic.content)  # 將 HTTP Response 物件的 content寫入檔案中
    f.close()  # 關閉檔案


def get_photolist(photo_name, download_num):
    page = 1  # 初始頁數為1
    photo_list = []  # 建立空的圖片 list

    url = "https://pixabay.com/zh/"  # Pixabay 網址
    option = webdriver.ChromeOptions()  # ←↓加入選項來指定不要有自動控制的訊息
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    browser = webdriver.Chrome(options=option)  # 以指定的選項啟動 Chrome
    # 連線到pixabay網頁, ●●注意, Chrome出現訊息窗時不可按【停用】鈕, 請按 x 將之關閉, 或不理它也可。
    browser.get(url)
    browser.find_element_by_name("q").send_keys(photo_name)
    browser.find_element_by_name("q").send_keys(Keys.RETURN)

    while True:
        html = browser.page_source
        #        print(html)
        bs = BeautifulSoup(html, "lxml")  # 解析網頁
        #  先尋找標籤為 div, calss 為 'flex_grid ...' 的元素 (這區中才是免費圖庫)
        #  再尋找所有標籤為 div, calss 為 'item' 的元素
        photo_item = bs.find(
            "div", {"class": "flex_grid credits search_results"}
        ).find_all("div", {"class": "item"})
        if len(photo_item) == 0:
            print("Error, no photo link in page", page)
            return None
        for i in range(len(photo_item)):
            # 尋找標籤 img 並取出 'src' 之中的內容
            photo = photo_item[i].find("img")["src"]
            if photo == "/static/img/blank.gif":
                # 尋找標籤 img 並取出 'data-lazy' 之中的內容
                photo = photo_item[i].find("img")["data-lazy"]
            if photo in photo_list:
                #                print('photo duplicated in photo_list at page', page, photo)
                continue
            # 若要下載較高解析度的圖, 可將下行取消註解
            #            photo = photo.replace('_340', '1280')  #更換為1280解析度
            photo_list.append(photo)  # 將找到的連結新增進 list 之中
            if len(photo_list) >= download_num:
                print("end by get photo list size", len(photo_list))
                browser.close()
                return photo_list
        page += 1  # 頁數加1
        # 找出下一頁的連結網址
        try:
            next = browser.find_element_by_partial_link_text("›").get_attribute("href")
            browser.get(next)
        except:  # 沒下一頁了
            browser.close()
            return photo_list


def create_folder(photo_name):
    folder_name = input("請輸入要儲存的資料夾名稱: ")

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print("資料夾不存在, 建立資料夾: " + folder_name)
    else:
        print("找到資料夾: " + folder_name)

    if not os.path.exists(folder_name + os.sep + photo_name):
        os.mkdir(folder_name + os.sep + photo_name)
        print("建立資料夾: " + photo_name)
    else:
        print(photo_name + " 資料夾已存在")
    return folder_name


def get_photobythread(folder_name, photo_name, photo_list):
    download_num = len(photo_list)  # 設定下載數量為圖片連結串列的長度
    Q = int(download_num / 100)  # 取商數
    R = download_num % 100  # 取餘數

    for i in range(Q):
        threads = []
        for j in range(100):
            threads.append(
                threading.Thread(
                    target=download_pic,
                    args=(
                        photo_list[i * 100 + j],
                        folder_name
                        + os.sep
                        + photo_name
                        + os.sep
                        + str(i * 100 + j + 1),
                    ),
                )
            )
            threads[j].start()
        for j in threads:
            j.join()
        print(int((i + 1) * 100 / download_num * 100), "%")  # 顯示當前進度

    threads = []
    for i in range(R):
        threads.append(
            threading.Thread(
                target=download_pic,
                args=(
                    photo_list[Q * 100 + i],
                    folder_name + os.sep + photo_name + os.sep + str(Q * 100 + i + 1),
                ),
            )
        )
        threads[i].start()
    for i in threads:
        i.join()
    print("100%")  # 顯示當前進度


print("------------------------------------------------------------")  # 60個

while True:
    photo_name = input("請輸入要下載的圖片名稱: ")

    download_num = int(input("請輸入要下載的數量: "))

    photo_list = get_photolist(photo_name, download_num)

    if photo_list == None:
        print("找不到圖片, 請換關鍵字再試試看")
    else:
        if len(photo_list) < download_num:
            print("找到的相關圖片僅有", len(photo_list), "張")
        else:
            print("取得所有圖片連結")
        break

folder_name = create_folder(photo_name)

print("開始下載...")

get_photobythread(folder_name, photo_name, photo_list)

print("\n下載完畢")

print("------------------------------------------------------------")  # 60個
