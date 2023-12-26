# ch6_38.py
string = "Abc"
# 正值索引
print(f" {string[0] = }",
      f"\n {string[1] = }",
      f"\n {string[2] = }")
# 負值索引
print(f" {string[-1] = }",
      f"\n {string[-2] = }",
      f"\n {string[-3] = }")
# 多重指定觀念
s1, s2, s3 = string
print(f"多重指定觀念的輸出測試 {s1}{s2}{s3}")


