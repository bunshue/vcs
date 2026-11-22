import sys
from pathlib import Path

print('測試修改檔案內容')
print('修改現在目錄下所有python檔案的內容')
print("------------------------------------------------------------")  # 60個

# 直接寫 Python 腳本批量修改

old_string = "david"
new_string = "peter"

for file in Path(".").rglob("*.py"):
    print(file)
    text = file.read_text(encoding="utf-8",errors="ignore")
    text = text.replace(old_string, new_string)
    file.write_text(text,encoding="utf-8")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

