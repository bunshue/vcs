# ch27_3.py
import PyPDF2

def encryptYorN(fn):
    '''檢查檔案是否加密'''
    pdfObj = open(fn,'rb')
    pdfRd = PyPDF2.PdfFileReader(pdfObj)
    if pdfRd.isEncrypted:       # 由這個屬性判斷是否加密
        print("%s 檔案有加密" % fn)
    else:
        print("%s 檔案沒有加密" % fn)

encryptYorN('travel.pdf')
encryptYorN('encrypttravel.pdf')








