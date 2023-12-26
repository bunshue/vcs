# ch4_21.py
fstream1 = open("d:\python\ch4\out1.txt", mode="w")     # 取代先前資料
print("Testing for output", file=fstream1)
fstream1.close( )
fstream2 = open("d:\python\ch4\out2.txt", mode="a") # 附加資料後面
print("Testing for output", file=fstream2)
fstream2.close( )



<script>

