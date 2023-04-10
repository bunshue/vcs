
import requests
from bs4 import BeautifulSoup

'''
此方法是使用yahoo字典檢視網頁原始碼查找要抓取的資料段落及屬性
然後將要的資料一層一層剖析出來
'''

def searchdic3(search_word):
    result = ''
    inp = 'lion'

    #yahoo字典的網址，可修改網址查詢想要的單字，網址當中的%s為格式化字串
    url = "https://tw.dictionary.search.yahoo.com/search?p=%s&fr2=dict" % (inp)
    html_data = requests.get(url)
    #print(url)

    soup = BeautifulSoup(html_data.text, "html.parser")
    #print(soup.prettify()) # 把排版後的 html 印出來

    try:
        mainBlock = soup.find_all('div', class_='grp grp-main pl-25')

        print(mainBlock)
        print(mainBlock[0].find_all('span', class_='fz-24 fw-500 c-black lh-24'))
        search_word = mainBlock[0].find_all('span', class_='fz-24 fw-500 c-black lh-24')
        print(search_word)
        
        # 查詢結果的整個區塊，用find_all方法找出所有div標籤且class屬性名稱為'dd algo explain mt-20 lst DictionaryResults'的資料
        # class_ 的"_"符號是因為class是保留字，所以加上_符號作區別
        
        allBlock = soup.find_all('div', class_='compTitle mt-25 mb-10')

        # yahoo字典的結果會依照詞性分作區塊，各個詞性的所有意思會被class為'compArticleList mb-15 ml-10'的ul標籤包在一起
        # 所以將上面allBlock的資料，以英文詞性區塊全部找出來，一樣使用find_all方法，找出ul標籤且屬性名稱為'compArticleList mb-15 ml-10'的資料
        meaningBlock = allBlock[0].find_all('span', class_='fz-24 fw-500 c-black lh-24')

        print('------------')
        print(meaningBlock)
        print('------------')
        
    except:
        print("查詢錯誤")
                  
    else:
        print('找出音標並print出來')
        pronunciation=soup.find_all('span',class_='fz-14')
        print(pronunciation[0].text)
        # 先找出詞性，詞性使用h3標籤，但在allBlock裡沒有其他h3標籤，所以就不指定class了
        parts = allBlock[0].find_all('h3')
        # 依照詞性數量的區塊做迴圈，將一個一個區塊作處理
        for i in range(len(meaningBlock)):
            # 顯示方面我們先顯示詞性值，後續再顯示單字意思
            print(parts[i].text)
            
            # 這個迴圈將詞性區塊裡的單字意思一個一個抓出來顯示
            # 而每個單字意思及例句都是使用li標籤所包起來，所以將每個li標籤抓出來顯示他的單字意思及例句
            for j in meaningBlock[i].find_all('li'):
                # 印出其中一個單字意思，單字意思是使用h4標籤，可如下對j抓取它的指定下一層標籤h4
                print("\t"+j.h4.text)
                hasES=False
                # 有些單字意思沒例句會出錯，所以對沒有例句的意思做例外跳過
                try:
                    #由於有些解釋有多個例句，因此去找所有例句
                    exampleSentence =j.find_all('span')
                    #第一個span會抓到中文意思，因此跳過，後面的例句每句後面都會多抓到一次中文解釋，因此k=k+2
                    for k in range(1, len(exampleSentence),2):
                        #有時會抓到雖然沒例句但是卻有span的時候，內容會是空白，因此過濾掉
                        if exampleSentence[k].text!=' ':
                            print("\t\t例句："+exampleSentence[k].text)
                            hasES=True
                except:
                    #跳過沒抓到span的
                    pass
                #如果沒例句時所作的處理
                if hasES==False:
                    print("\t\t沒例句。")


def example03():
    print('Yahoo字典3')
    search_word3 = 'oat'
    #search_word3 = '英國'
    searchdic3(search_word3)

example03()


                




