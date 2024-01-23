"""
pip install pdfminer.six

"""

from pdfminer.high_level import extract_text

infile = "test.pdf"
try:
    text = extract_text(infile)     #擷取文字
    print(text)
except:
    print("程式執行失敗")
