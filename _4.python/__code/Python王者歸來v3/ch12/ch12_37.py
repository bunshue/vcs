# ch12_37.py
# 定義 StudentManager 類別來管理學生資料
class StudentManager:
    # 初始化方法, 建立一個空的學生字典
    def __init__(self):
        self.students = {}          # 學生字典,鍵是學生ID,值是學生名字

    # 方法用於添加新學生到字典中
    def add_student(self, id, name):
        self.students[id] = name    # 添加學生

    # 移除指定ID的學生, 檢查學生ID是否存在，如果存在則移除
    def remove_student(self, id):
        if id in self.students:
            del self.students[id]

# 使用 StudentManager 類別來管理學生
manager = StudentManager()          # 建立 StudentManager 物件
manager.add_student(1, 'Hung')      # 添加學生 Hung
manager.remove_student(1)           # 移除學生ID為 1 的學生

# 用 print(manager.students) 來查看學生字典的當前狀態
print(manager.students)             # 輸出：{}


