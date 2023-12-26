# ch11_47.py
def event_handler(event):
    def register_handler(handler_function):
        print(f"處理(Handling) {event} with {handler_function.__name__}")
        handler_function(event)
    return register_handler

def on_click(event):                # 按一下
    print(f"按一下 : {event}")

def on_hover(event):                # 懸停留
    print(f"懸停留 : {event}")

# 創建事件處理器
click_handler = event_handler("按一下事件")
hover_handler = event_handler("懸停留事件")

# 註冊和觸發事件
click_handler(on_click)
hover_handler(on_hover)


