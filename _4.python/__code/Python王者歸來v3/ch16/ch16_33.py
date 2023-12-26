# ch16_33.py
import re                   

# 定義一個函數用於重命名檔案串列
def rename_files(files):
    # 定義正則表達式模式匹配檔案名的一部分
    # (\w+)   匹配一個或多個單詞字元(字母、數字或底線)
    # (\d{4}) 匹配四位數字 (代表年份)
    # (\d{2}) 匹配兩位數字 (代表月份)
    pattern = r"(\w+)_(\d{4})_(\d{2})"
    for file in files:                              # 遍歷檔案串列
        # 使用 sub() 函數替換匹配的名稱
        # \1, \2, \3 分別對應第一、第二、第三個捕獲組匹配的內容
        # 這裡將 底線( _ ) 替換為 ( - )
        new_name = re.sub(pattern, r"\1-\2-\3", file)
        print(f"Old : {file},   New: {new_name}")   # 輸出舊和新檔名

# 檔案名稱串列
files = [
    "report_2023_04.pdf",
    "report_2023_05.pdf",
    "summary_2023_04.docx"
]

rename_files(files)  # 呼叫函數, 傳入檔案名稱串列

# 輸出
# Old: report_2023_04.pdf,  New: report-2023-04.pdf
# Old: report_2023_05.pdf,  New: report-2023-05.pdf
# Old: summary_2023_04.docx,  New: summary-2023-04.docx





