import chatBot_module as m

question = ""
answer = ""
QA = {"你是誰": "我是萱萱", "聽不懂": "請再說一次問題"}

print("請說話")
question = m.bot_listen()  # 打開耳朵聽問題
print(question)

if question in QA:  # 如果問題存於 QA 字典中
    answer = QA[question]
    m.bot_speak(answer, "zh-tw")
    print(answer)
else:  # 問題不存於 QA 字典中, 進行網路爬蟲
    keyword = m.bot_get_google(question)
    content = m.bot_get_wiki(keyword)
    if content != None:
        print("要結束請連續按 ctrl+c")
        m.bot_speak_re(content)
    else:
        print("找不到相關的維基百科資料")
