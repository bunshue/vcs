# ch11_25_5g.py
def event_handler(event):
    def register_handler(handler_function):
        print(f"Handling {event} with {handler_function.__name__}")
        handler_function(event)
    return register_handler

def on_click(event):
    print(f"Clicked: {event}")

def on_hover(event):
    print(f"Hovered: {event}")

# 創建事件處理器
click_handler = event_handler("Click Event")
hover_handler = event_handler("Hover Event")

# 註冊和觸發事件
click_handler(on_click)
hover_handler(on_hover)


