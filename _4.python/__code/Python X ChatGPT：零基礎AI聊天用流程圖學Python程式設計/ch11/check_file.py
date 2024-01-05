import os

def check_txt_file(file_path):
    """
    檢查指定路徑的檔案是否存在，如果存在就回傳True；不存在就回傳False。
    """
    if os.path.isfile(file_path) and file_path.endswith(".txt"):
        return True
    else:
        return False

