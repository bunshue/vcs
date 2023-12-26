# ch6_45.py
string = "Python"
# 正值索引
print(f" {string[0] = }",
      f"\n {string[1] = }",
      f"\n {string[2] = }",
      f"\n {string[3] = }",
      f"\n {string[4] = }",
      f"\n {string[5] = }")
# 負值索引
print(f" {string[-1] = }",
      f"\n {string[-2] = }",
      f"\n {string[-3] = }",
      f"\n {string[-4] = }",
      f"\n {string[-5] = }",
      f"\n {string[-6] = }")
# 多重指定觀念
s1, s2, s3, s4, s5, s6 = string
print("多重指定觀念的輸出測試 = ",s1,s2,s3,s4,s5,s6)


