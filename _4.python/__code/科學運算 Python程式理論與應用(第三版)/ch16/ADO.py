# -*- coding:utf-8 -*-
# file: ADO.py
#
import win32com.client								# 匯入win32com.client
adoCon = win32com.client.Dispatch('ADODB.Connection')				# 建立連線物件
adoCon.Open('podbc')  								# 連線到資料源
adoRS = win32com.client.Dispatch('ADODB.Recordset')				# 建立Recordset物件
adoRS.Open('[' + 'people' + ']', adoCon, 1, 3)					# 開啟資料源中的people表
adoRS.MoveFirst()								# 搬移到第一條記錄
for i in range(adoRS.RecordCount):
	print(adoRS.Fields('name').Value)					# 輸出記錄的name
	print(adoRS.Fields('age').Value)						# 輸出記錄的age
	print(adoRS.Fields('sex').Value)						# 輸出記錄的sex
	adoRS.MoveNext()
adoRS.AddNew()									# 加入新記錄
adoRS.Fields('name').Value = 'Kate'						# 新記錄的name
adoRS.Fields('age').Value = 22							# 新記錄的age
adoRS.Fields('sex').Value = 'Female'						# 新記錄的sex
adoRS.Update()									# 更新記錄
adoRS.Close()									# 關閉表
adoCon.Close()									# 關閉資料庫連線
