from pathlib import Path

filepath = "test1.txt"
p = Path(filepath)
print("檔案路徑　　　 = " + str(p))
print("檔案名稱　　　　 = " + p.name)
print("檔案副檔名　　 = " + p.suffix)
print("檔案副檔名以外 = " + p.stem)
print("資料夾名稱　　　　 = " + p.parent.name)
print("檔案大小　　 = " + str(p.stat().st_size) + "位元組")
