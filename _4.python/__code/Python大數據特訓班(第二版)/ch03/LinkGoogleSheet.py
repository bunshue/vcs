import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac
# 設定金鑰檔路徑及驗證範圍
auth_json = 'PythonConnectGsheet1-6a6086d149c5.json'
gs_scopes = ['https://spreadsheets.google.com/feeds']
# 連線資料表
cr = sac.from_json_keyfile_name(auth_json, gs_scopes)
gc = gspread.authorize(cr) 
# 開啟資料表
spreadsheet_key = '1OihpM657yWo1lc3RjskRfZ8m75dCPwL1IPwoDXSvyzI' 
sheet = gc.open_by_key(spreadsheet_key)
# 開啟工作簿
wks = sheet.sheet1
# 清除所有內容
wks.clear() 
# 新增列
listtitle=['座號', '姓名', '國文', '英文', '數學']
wks.append_row(listtitle)  # 標題
listdatas=[[1, '葉大雄', 65, 62, 40],
           [2, '陳靜香', 85, 90, 87],
           [3, '王聰明', 92, 90, 95]]
for listdata in listdatas:
    wks.append_row(listdata)  # 資料內容