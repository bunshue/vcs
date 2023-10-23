import zipfile

with zipfile.ZipFile('檔案路徑.zip', 'r') as zip_ref:
    zip_ref.extractall('解壓縮目標資料夾')




