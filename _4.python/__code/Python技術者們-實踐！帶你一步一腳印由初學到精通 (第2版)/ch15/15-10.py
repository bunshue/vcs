import chatBot_module as m

question = ''
answer = ''
QA = {'你是誰' : '我是萱萱', '聽不懂' : '請再說一次問題'}

question = m.bot_listen()        # 打開耳朵聽問題
print(question)
if question in QA:               # 如果問題存於 QA 字典中
    answer = QA[question]        # 取出問題的答案
    m.bot_speak(answer, 'zh-tw') # 唸出答案
    print(answer)
else:                            # 問題不存於 QA 字典中, 進行網路爬蟲
    print('進行網路爬蟲')         # 爬蟲功能稍後加入