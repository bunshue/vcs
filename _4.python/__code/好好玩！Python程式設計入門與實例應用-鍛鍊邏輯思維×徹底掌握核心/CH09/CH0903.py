# 宣告類別
class student():
    def score(self, s1, s2, s3):
        return (s1 + s2 + s3)/3

# 產生物件
vicky = student()
# 呼叫score()方法並傳入引數
average = vicky.score(98, 65, 81)
print(f'Vicky 平均分數：{average:.3f}')
