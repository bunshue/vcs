# ch4_13.py
score = 90
name = "洪錦魁"
count = 1
# 以下鼓勵使用
print("{0}你的第 {1} 次物理考試成績是 {2}".format(name,count,score))

# 以下語法對但不鼓勵使用
print("{2}你的第 {1} 次物理考試成績是 {0}".format(score,count,name))


