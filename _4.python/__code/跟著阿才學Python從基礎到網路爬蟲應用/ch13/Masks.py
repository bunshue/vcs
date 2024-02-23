import requests, csv, os

def fnDownloadCsv(): #下載CSV檔
    print('口罩資料下載中...')
    # 健保特約機構口罩剩餘數量明細清單資料來源的Url
    maskdataUrl = 'https://data.nhi.gov.tw/resource/mask/maskdata.csv'
    # 下載健保特約機構口罩剩餘數量明細清單資料並儲存成Masks.csv
    r = requests.get(maskdataUrl) 
    f = open("Masks.csv", "wb")
    f.write(r.content)
    f.close()
    print('口罩資料下載完成...')
    
def fnShowResult():
    # 將輸入地址有 '台' 的字換成 '臺'
    search=str(input('請搜尋藥局地址:'))
    search=search.replace('台','臺')
    print('='*50) 
    # 開啟Masks.csv資料檔，並將口罩資料轉成data字典物件
    f=open('Masks.csv',encoding='utf-8') 
    data=csv.DictReader(f) 
    # 若有Masks.html網頁即刪除
    if os.path.exists("Masks.html"):
        os.remove('Masks.html')
    # 使用附加模式建立Masks.html網頁
    fH=open('Masks.html', 'a',encoding="utf-8")      
    # 寫入網頁表格標題
    fH.write('<meta charset="utf-8" /><table border="1">')  
    fH.write('<tr>\
                 <th>醫事機構名稱</th>\
                 <th>醫事機構地址</th>\
                 <th>醫事機構電話</th>\
                 <th>成人口罩剩餘數</th>\
                 <th>兒童口罩剩餘數</th>\
                 <th>路線規劃</th>\
              </tr>')
    # 印出查詢的健保特約機構口罩剩餘數量明細資料
    for row in data:  
         address=row['醫事機構地址']
         #判斷地址與搜尋地址是否吻合
         if (search in address) : 
             #不顯示成人以及兒童口罩賣完的診所
             if row['成人口罩剩餘數']!=0 and row['兒童口罩剩餘數']!=0:
                    print('藥局名稱:',row['醫事機構名稱'])
                    print('藥局地址:',row['醫事機構地址'])
                    print('藥局電話:',row['醫事機構電話'])
                    print('成人口罩剩餘數:',row['成人口罩剩餘數'])
                    print('兒童口罩剩餘數:',row['兒童口罩剩餘數'])
                    print('='*50)      
                    # 將資料寫入Masks.html
                    fH.write('<tr>')
                    fH.write('<td>'+row['醫事機構名稱']+'</td>')
                    fH.write('<td>'+row['醫事機構地址']+'</td>')
                    fH.write('<td>'+row['醫事機構電話']+'</td>')
                    fH.write('<td>'+row['成人口罩剩餘數']+'</td>')
                    fH.write('<td>'+row['兒童口罩剩餘數']+'</td>')
                    fH.write('<td><a href="https://www.google.com/' + 
                             'maps/search/'+row['醫事機構地址']+'">路線規劃</a></td>')
                    fH.write('</tr>')
    fH.write('</table>')
    # 關閉檔案
    fH.close()
    f.close() 
    os.system('Masks.html')
    
fnDownloadCsv() # 呼叫fnDownLoadCsv()函式下載健保特約機構口罩剩餘數量明細清單
fnShowResult()  # 印出查詢的健保特約機構口罩剩餘數量明細資料並建立成網頁檔