

import wikipedia, sys

wikipedia.set_lang('zh')

try:
    summary = wikipedia.summary(sys.argv[1], sentences=1)
    print(summary)
except IndexError:
    print("請在執行此程式時提供一個查詢主題。例如：\npython wiki_sample_final.py Python")






