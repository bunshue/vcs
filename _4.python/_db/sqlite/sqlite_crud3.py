"""
"""
import shutil
import sqlite3
import datetime

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    # return
    plt.tight_layout()  # 緊密排列, 並填滿原圖大小
    plt.show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, "rb") as file:
        blobData = file.read()
    return blobData


def insertBLOB(empId, name, photo, resumeFile):
    try:
        conn = sqlite3.connect("tmp_SQLite_Python.db")  # 建立資料庫連線
        cursor = conn.cursor()  # 建立 cursor 物件
        sqlstr = """
        CREATE TABLE IF NOT EXISTS table01(
        idx    INTEGER PRIMARY KEY,
        name   TEXT NOT NULL,
        photo  BLOB,
        resume BLOB
        )
        """
        cursor.execute(sqlstr)
        conn.commit()  # 更新

        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO table01
                                  (idx, name, photo, resume) VALUES (?, ?, ?, ?)"""

        empPhoto = convertToBinaryData(photo)
        resume = convertToBinaryData(resumeFile)
        # Convert data into tuple format
        data_tuple = (empId, name, empPhoto, resume)
        cursor.execute(sqlite_insert_blob_query, data_tuple)  # fail在此
        conn.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("the sqlite connection is closed")


pic_filename1 = (
    "D:/_git/vcs/_1.data/______test_files1/__pic/_anime/_angry_bird/AB_red.jpg"
)
pic_filename2 = (
    "D:/_git/vcs/_1.data/______test_files1/__pic/_anime/_angry_bird/AB_blue.jpg"
)
resume1 = "D:/_git/vcs/_1.data/______test_files1/_case1/_case1a/eula.3081.txt"
resume2 = "D:/_git/vcs/_1.data/______test_files1/_case1/_case1a/eula.3082.txt"

# pic_filename1 = "aa.jpg"
# pic_filename2 = "bb.jpg"
# resume1 = "tt1.txt"
# resume2 = "tt2.txt"


insertBLOB(1, "Red Bird", pic_filename1, resume1)
insertBLOB(2, "Blue Bird", pic_filename2, resume1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, "wb") as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")


def readBlobData(empId):
    try:
        conn = sqlite3.connect("tmp_SQLite_Python.db")
        cursor = conn.cursor()
        print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * from table01 where idx = ?"""
        cursor.execute(sql_fetch_blob_query, (empId,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name = row[1]
            photo = row[2]
            resumeFile = row[3]

            print("Storing employee image and resume on disk \n")
            photoPath = "tmp_" + name + ".jpg"
            resumePath = "tmp_" + name + "_resume.txt"
            writeTofile(photo, photoPath)
            writeTofile(resumeFile, resumePath)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if conn:
            conn.close()
            print("sqlite connection is closed")


readBlobData(1)
readBlobData(2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
