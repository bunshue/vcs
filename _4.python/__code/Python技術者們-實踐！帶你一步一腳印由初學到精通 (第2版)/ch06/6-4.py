def get_setting():    #←將「讀取設定檔」寫成函式, 可讓程式易讀易用
	res = []     #←準備一個空串列來存放讀取及解析的結果
	try:              # 使用 try 來預防開檔或讀檔錯誤
		with open('stock.txt') as f:  # 用 with 以讀取模式開啟檔案
			slist = f.readlines()     # 以行為單位讀取所有資料
			print('讀入：', slist)    # 輸出讀到的資料以供確認
			a, b, c = slist[0].split(',')   #←將股票字串以逗號切割為串列
			res = [a, b, c]
	except:
		print('stock.txt 讀取錯誤')
	return res   #←傳回解析的結果, 但如果開檔或讀檔錯誤則會傳回 []

stock = get_setting()     # 呼叫上面的函式
print('傳回：', stock)    # 輸出傳回的結果
