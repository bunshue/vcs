# ch16_35.py
import re

def clean_text(text):
    # 刪除不可列印字元和特殊符號, 只保留字母、數字和空格
    pattern = r"[^\w\s]"
    cleaned_text = re.sub(pattern, "", text)
    return cleaned_text

dirty_data = "Name: John Doe; Age: 30; %Salary: $5000"
print(clean_text(dirty_data))
# 輸出: Name John Doe Age 30 Salary 5000


