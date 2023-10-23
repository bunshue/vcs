import zipfile

with zipfile.ZipFile('檔案路徑.zip', 'w') as zipf:
    zipf.write('要壓縮的檔案路徑', arcname='壓縮檔案中的名稱')




