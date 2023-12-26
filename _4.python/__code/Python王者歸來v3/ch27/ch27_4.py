# ch27_4.py
import PyPDF2

def encryptYorN(fn):
    '''檢查檔案是否加密'''
    with open(fn,'rb') as file:     
        pdfRd = PyPDF2.PdfReader(file)  # 讀 pdf
        if pdfRd.is_encrypted:          # 由這個屬性判斷是否加密
            print(f"{fn:17s} : 檔案有加密")
        else:
            print(f"{fn:17s} : 檔案沒有加密")

encryptYorN('travel.pdf')
encryptYorN('encrypttravel.pdf')








