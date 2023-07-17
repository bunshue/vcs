import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac
# 設定金鑰檔路徑及驗證範圍
auth_json = 'pythonconnectgsheet1-273500-e6ce04448957.json'
gs_scopes = ['https://spreadsheets.google.com/feeds']
# 連線資料表
cr = sac.from_json_keyfile_name(auth_json, gs_scopes)
gs_client = gspread.authorize(cr) 
# 開啟資料表
spreadsheet_key = '1lBlHPDYqwnQNiJrz-8nqPEd5H6Q4w0PaKasrrjojCNI' 
sheet = gs_client.open_by_key(spreadsheet_key)
# 開啟工作簿
wks = sheet.sheet1
# 清除所有內容
wks.clear() 
# 新增列
listtitle=["姓名","電話"]
wks.append_row(listtitle)  # 標題
listdata=["chiou","0937-1234567"]
wks.append_row(listdata)   # 資料內容