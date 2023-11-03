# -*- coding:utf-8 -*-
# file: DAO.py
#
import win32com.client								# 匯入win32com.client
dbEngine = win32com.client.Dispatch('DAO.DBEngine.36')				# 連線COM物件
daoDB = dbEngine.OpenDatabase('e:\python\第16章\python.accdb')					# 開啟資料庫
daoRS = daoDB.OpenRecordset('people')						# 開啟表
daoRS.MoveLast()     								# 搬移到最後一條記錄
print( daoRS.RecordCount)								# 輸出記錄總數
print( daoRS.Fields('name').Value)						# 輸出最後一條記錄的name
print (daoRS.Fields('age').Value)						# 輸出最後一條記錄的age
print (daoRS.Fields('sex').Value	)						# 輸出最後一條記錄的sex
daoRS.AddNew()									# 加入新記錄
daoRS.Fields('name').Value = 'Kate'						# 新記錄的name
daoRS.Fields('age').Value = 22							# 新記錄的age
daoRS.Fields('sex').Value = 'Female'						# 新記錄的sex
daoRS.Update()									# 更新記錄
daoRS.Close()									# 關閉表
daoDB.Close()									# 關閉資料庫連線
