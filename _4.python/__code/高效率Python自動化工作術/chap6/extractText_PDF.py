from pathlib import Path
from pdfminer.high_level import extract_text

infile = "test.pdf"

#【函數: 從PDF檔案擷取Text】
def extracttext(readfile):
    try:
        text = extract_text(readfile)
        return text
    except:
        return readfile + "：程式執行失敗。"
    
#【執行函數】
msg = extracttext(infile)
print(msg)