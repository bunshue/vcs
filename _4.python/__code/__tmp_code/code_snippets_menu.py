from thonny import get_workbench
# from tkinter.messagebox import showinfo
import tkinter as tk

# 將程式碼插入編輯標籤頁
def insert_py_code_into_editor(editor_text, py_code):
    # 判斷是否有選取內容, 有就是取代
    if editor_text.tag_ranges(tk.SEL):
        ori_sel_first = editor_text.index(tk.SEL_FIRST)
        ori_sel_last = editor_text.index(tk.SEL_LAST)
        # 刪除選取
        editor_text.tag_remove(tk.SEL, tk.SEL_FIRST, tk.SEL_LAST)
        # 刪除內容
        editor_text.delete(ori_sel_first, ori_sel_last)
    # 插入程式碼        
    py_code_insert(editor_text, py_code)
    
# 插入多行程式碼
def py_code_insert(text_widget, code_content):
    lines = code_content.split('\n')  
    line_num = len(lines)          
    if line_num == 1 :   # 單行程式碼
        text_widget.insert(tk.INSERT, lines[0])
        text_widget.event_generate("<Return>")
    elif line_num > 1 :  # 多行程式碼 
        line_count = len(lines)
        for i, line in enumerate(lines):
            text_widget.insert(tk.INSERT, line)  
            text_widget.event_generate("<Return>")  

# 動作符號選單-事件處理
def item_declar_var():     
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()    
    insert_py_code_into_editor(editor.get_code_view().text, "var1 = None")

def item_assign_int():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()   
    insert_py_code_into_editor(editor.get_code_view().text, "var1 = 20")

def item_assign_float():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()    
    insert_py_code_into_editor(editor.get_code_view().text, "var1 = 12.3")
    
def item_assign_str():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()    
    insert_py_code_into_editor(editor.get_code_view().text, "var1 = \"Hello!\"")
    
def item_assign_var():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()    
    insert_py_code_into_editor(editor.get_code_view().text, "var1 = var2")

def item_exp_add():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "result = var1 + var2")

def item_exp_subtract():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "result = var1 - var2")

def item_exp_multiply():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "result = var1 * var2")

def item_exp_divide():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "result = var1 / var2")

def item_exp_mod():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "result = var1 % var2")

# 輸出/輸入符號選單-事件處理
def item_write():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "print(\"Hello World!\", end=\"\")")

def item_write_line():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "print(\"Hello World!\")")

def item_write_var():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "print(\"var1 = \", var1, end=\"\")")      
    
def item_write_var2():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "print(\"var1 = \" + str(var1), end=\"\")")    

def item_write_line_var():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "print(\"var1 = \", var1)")      
    
def item_write_line_var2():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "print(\"var1 = \" + str(var1))")  

def item_write_var_only():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "print(var1, end=\"\")")

def item_write_line_var_only():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "print(var1)")

def item_input_int():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "var1 = int(input(\"Please enter an integer =>\"))")
    
def item_input_float():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "var1 = float(input(\"Please enter a floating point number =>\"))")

def item_input_str():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "var1 = input(\"Please enter a string =>\")")

# 決策符號-條件選單-事件處理
def item_if():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "if var1 >= 10:\nprint(\"condition is true\")")

def item_if_else():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "if var1 >= 10:\nprint(\"condition is true\")")
    editor.get_code_view().text.event_generate("<BackSpace>")
    insert_py_code_into_editor(editor.get_code_view().text, "else:\nprint(\"condition is false\")")

def item_if_elif_else():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "if var1 >= 20:\nprint(\"this condition is true\")")
    editor.get_code_view().text.event_generate("<BackSpace>")
    insert_py_code_into_editor(editor.get_code_view().text, "elif var1 >= 10: \nprint(\"this condition is true\")")
    editor.get_code_view().text.event_generate("<BackSpace>")    
    insert_py_code_into_editor(editor.get_code_view().text, "else: \nprint(\"conditions are false\")")

# 決策符號-迴圈選單-事件處理
def item_loop_for():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "for i in range(1, 11):\nprint(\"i = \" + str(i))")

def item_loop_while():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "i = 1\nwhile i <= 10:\nprint(\"i = \" + str(i))\ni = i + 1");

def item_loop_break():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "if i > 5:\nbreak")

def item_loop_continue():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "if i % 2 == 0:\ncontinue")

# 程序/函數選單-事件處理
def item_sub_def():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "def mySub(para1, para2):\nprint(\"statements to be executed\")")

def item_sub_call():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "mySub(para1, para2)")

def item_func_def():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "def myFunc(para1, para2):\nprint(\"statements to be executed\")\nreturn para1 + para2")

def item_func_call():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "result = myFunc(para1, para2)")

# 海龜繪圖選單-事件處理
def item_turtle_import():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "import turtle")

def item_turtle_screen_sleep():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.exitonclick() # Click Screen to quit.\nturtle.bye()")
    
def item_turtle_windowsize():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.setup(640, 480, 10, 10) # width, height, startx, starty")

def item_turtle_screensize():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.screensize(480, 360, \"yellow\") # width, height, bgcolor")

def item_turtle_forward():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.forward(x)")

def item_turtle_backward():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.back(x)")

def item_turtle_turnleft():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.left(x)")

def item_turtle_turnright():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.right(x)")

def item_turtle_color():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.color(\"blue\")")

def item_turtle_icon():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.shape(\"turtle\")")

def item_turtle_goto():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.goto(-50, -50)")

def item_turtle_setx():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.setx(100)")

def item_turtle_sety():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.sety(-100)")

def item_turtle_setheading():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.setheading(90)")

def item_turtle_penup():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.penup()")

def item_turtle_pendown():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.pendown()")

def item_turtle_pensize():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.pensize(5)")
    
def item_turtle_pencolor():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.pencolor(\"blue\")")

def item_turtle_fillcolor():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.fillcolor(\"red\")")

def item_turtle_begin_fill():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.begin_fill()")
    
def item_turtle_end_fill():
    editor = get_workbench().get_editor_notebook().get_current_editor()
    if editor is None:
        return None
    editor.get_code_view().focus_set()
    insert_py_code_into_editor(editor.get_code_view().text, "turtle.end_fill()")    

def load_plugin():
    # showinfo("Hello", get_workbench().get_option("general.language"))
    lang_index = 0   # 0 繁體中文; 1是英文; 2是簡體中文
    
    lang_code = get_workbench().get_option("general.language")
    
    if lang_code == "zh_TW":
        lang_index = 0           # 繁體
    elif lang_code == "zh_CN":
        lang_index = 2           # 簡體
    else:
        lang_index = 1           # 英文
        
    menu_action = {
         "title": ["動作符號", "Action", "动作符号"],
         "items":[
                  ["宣告變數", "Declare variables", "声明变量"], 
                  ["指定成整數值", "Assign int value to variable", "指定成整数值"], 
                  ["指定成浮點數值", "Assign float value to variable", "指定成浮点数值"], 
                  ["指定成字串值", "Assign string value to variable", "指定成字符串值"], 
                  ["指定成其他變數", "Assign variable value to another variable", "指定成其他变量"],
                  ["算術運算式: 加法", "Arithmetic expression: Addition", "算术表达式: 加法"], 
                  ["算術運算式: 減法", "Arithmetic expression: Subtraction", "算术表达式: 减法"], 
                  ["算術運算式: 乘法", "Arithmetic expression: Multiplication", "算术表达式: 乘法"], 
                  ["算術運算式: 除法", "Arithmetic expression: Division", "算术表达式: 除法"],          
                  ["算術運算式: 餘數", "Arithmetic expression: Remainder", "算术表达式: 余数"]
                ]
    }
    # 動作符號選單
    # 宣告變數群組
    get_workbench().add_command(command_id="item_declar_var",
                                menu_name=menu_action["title"][lang_index],
                                command_label=menu_action["items"][0][lang_index],
                                handler=item_declar_var, 
                                group=100)
    # 指定敘述群組                            
    get_workbench().add_command(command_id="item_assign_int",
                                menu_name=menu_action["title"][lang_index],
                                command_label=menu_action["items"][1][lang_index],
                                handler=item_assign_int,
                                group=110)
    get_workbench().add_command(command_id="item_assign_float",
                                menu_name=menu_action["title"][lang_index],
                                command_label=menu_action["items"][2][lang_index],
                                handler=item_assign_float,
                                group=110)                            
    get_workbench().add_command(command_id="item_assign_str",
                                menu_name=menu_action["title"][lang_index],
                                command_label=menu_action["items"][3][lang_index],
                                handler=item_assign_str,
                                group=110)
    get_workbench().add_command(command_id="item_assign_var",
                                menu_name=menu_action["title"][lang_index],
                                command_label=menu_action["items"][4][lang_index],
                                handler=item_assign_var,
                                group=110)                           
    # 算術運算式群組 
    get_workbench().add_command(command_id="item_exp_add",
                                menu_name=menu_action["title"][lang_index],
                                command_label=menu_action["items"][5][lang_index],
                                handler=item_exp_add,
                                group=120)
    get_workbench().add_command(command_id="item_exp_subtract",
                                menu_name=menu_action["title"][lang_index],
                                command_label=menu_action["items"][6][lang_index],
                                handler=item_exp_subtract,
                                group=120)                            
    get_workbench().add_command(command_id="item_exp_multiply",
                                menu_name=menu_action["title"][lang_index],
                                command_label=menu_action["items"][7][lang_index],
                                handler=item_exp_multiply,
                                group=120)    
    get_workbench().add_command(command_id="item_exp_divide",
                                menu_name=menu_action["title"][lang_index],
                                command_label=menu_action["items"][8][lang_index],
                                handler=item_exp_divide,
                                group=120)                            
    get_workbench().add_command(command_id="item_exp_mod",
                                menu_name=menu_action["title"][lang_index],
                                command_label=menu_action["items"][9][lang_index],
                                handler=item_exp_mod,
                                group=120)        
    menu_io = {
         "title": ["輸入和輸出符號", "I/O", "输出和输入符号"],
         "items":[
                  ["輸出符號: 訊息文字+不換行", "Output symbol: Message+no LF", "输出符号: 消息文本+不换行"], 
                  ["輸出符號: 訊息文字+換行", "Output symbol: Message+LF", "输出符号: 消息文本+换行"],
                  ["輸出符號: 訊息文字+變數+不換行( , )", "Output symbol: Message+Variable+no LF( , )", "输出符号: 消息文本+变量+不换行( , )"],
                  ["輸出符號: 訊息文字+變數+換行( , )", "Output symbol: Message+Variable+LF( , )", "输出符号: 消息文本+变量+换行( , )"],
                  ["輸出符號: 訊息文字+變數+不換行( + )", "Output symbol: Message+Variable+no LF( + )", "输出符号: 消息文本+变量+不换行( + )"],                  
                  ["輸出符號: 訊息文字+變數+換行( + )", "Output symbol: Message+Variable+LF( + )", "输出符号: 消息文本+变量+换行( + )"],
                  ["輸出符號: 變數+不換行", "Output symbol: Variable+no LF", "输出符号: 变量+不换行"],
                  ["輸出符號: 變數+換行", "Output symbol: Variable+LF", "输出符号: 变量+换行"],
                  ["輸入符號: 輸入整數", "Input symbol: Input int", "输入符号: 输入整数值"],
                  ["輸入符號: 輸入浮點數", "Input symbol: Input float", "输入符号: 输入浮点数值"],
                  ["輸入符號: 輸入字串", "Input symbol: Input string", "输入符号: 输入字符串"]                 
                ]
    }    
    # 輸入/輸出符號選單
    # 輸出符號群組
    get_workbench().add_command(command_id="item_write",
                                menu_name=menu_io["title"][lang_index],
                                command_label=menu_io["items"][0][lang_index],
                                handler=item_write, 
                                group=100)                           
    get_workbench().add_command(command_id="item_write_line",
                                menu_name=menu_io["title"][lang_index],
                                command_label=menu_io["items"][1][lang_index],
                                handler=item_write_line,
                                group=100)    
    get_workbench().add_command(command_id="item_write_var",
                                menu_name=menu_io["title"][lang_index],
                                command_label=menu_io["items"][2][lang_index],
                                handler=item_write_var, 
                                group=100)   
    get_workbench().add_command(command_id="item_write_line_var",
                                menu_name=menu_io["title"][lang_index],
                                command_label=menu_io["items"][3][lang_index],
                                handler=item_write_line_var,
                                group=100)                                    
    get_workbench().add_command(command_id="item_write_var2",
                                menu_name=menu_io["title"][lang_index],
                                command_label=menu_io["items"][4][lang_index],
                                handler=item_write_var2, 
                                group=100) 
    get_workbench().add_command(command_id="item_write_line_var2",
                                menu_name=menu_io["title"][lang_index],
                                command_label=menu_io["items"][5][lang_index],
                                handler=item_write_line_var2,
                                group=100)
    get_workbench().add_command(command_id="item_write_var_only",
                                menu_name=menu_io["title"][lang_index],
                                command_label=menu_io["items"][6][lang_index],
                                handler=item_write_var_only, 
                                group=100)                           
    get_workbench().add_command(command_id="item_write_line_var_only",
                                menu_name=menu_io["title"][lang_index],
                                command_label=menu_io["items"][7][lang_index],
                                handler=item_write_line_var_only,
                                group=100)
    # 輸入符號群組     
    get_workbench().add_command(command_id="item_input_int",
                                menu_name=menu_io["title"][lang_index],
                                command_label=menu_io["items"][8][lang_index],
                                handler=item_input_int,
                                group=110)    
    get_workbench().add_command(command_id="item_input_float",
                                menu_name=menu_io["title"][lang_index],
                                command_label=menu_io["items"][9][lang_index],
                                handler=item_input_float,
                                group=110)        
    get_workbench().add_command(command_id="item_input_str",
                                menu_name=menu_io["title"][lang_index],
                                command_label=menu_io["items"][10][lang_index],
                                handler=item_input_str,
                                group=110)        
    
    menu_condition = {
         "title": ["決策符號-條件", "Decision-conditions", "决策符号-条件"],
         "items":[
                  ["If單選條件", "If conditions", "If单选条件"], 
                  ["If/Else二選一條件", "If/Else conditions", "If/Else二选一条件"],
                  ["If/Elif/Else多選一條件", "If/Elif/Else Multiple selection conditions", "If/Elif/Else多选一条件"],
                ]
    }    
    # 決策符號-條件選單
    get_workbench().add_command(command_id="item_if",
                                menu_name=menu_condition["title"][lang_index],
                                command_label=menu_condition["items"][0][lang_index],
                                handler=item_if, 
                                group=100)                           
    get_workbench().add_command(command_id="item_if_else",
                                menu_name=menu_condition["title"][lang_index],
                                command_label=menu_condition["items"][1][lang_index],
                                handler=item_if_else,
                                group=100)    
    get_workbench().add_command(command_id="item_if_elif_else",
                                menu_name=menu_condition["title"][lang_index],
                                command_label=menu_condition["items"][2][lang_index],
                                handler=item_if_elif_else, 
                                group=100)                               
    
    menu_loop = {
         "title": ["決策符號-迴圈", "Decision-loop", "决策符号-循环"],
         "items":[
                  ["前測式迴圈: For迴圈", "Pre-conditions loop: For loop", "前测式循环: For循环"], 
                  ["前測式迴圈: While迴圈", "Pre-conditions loop: While loop", "前测式循环: While循环"],
                  ["跳出迴圈", "Break loop", "跳出循环"],
                  ["繼續迴圈", "Continue loop", "继续循环"]
                ]
    }  
    # 決策符號-迴圈選單
    get_workbench().add_command(command_id="item_loop_for",
                                menu_name=menu_loop["title"][lang_index],
                                command_label=menu_loop["items"][0][lang_index],
                                handler=item_loop_for, 
                                group=100)                           
    get_workbench().add_command(command_id="item_loop_while",
                                menu_name=menu_loop["title"][lang_index],
                                command_label=menu_loop["items"][1][lang_index],
                                handler=item_loop_while,
                                group=100)    
    get_workbench().add_command(command_id="item_loop_break",
                                menu_name=menu_loop["title"][lang_index],
                                command_label=menu_loop["items"][2][lang_index],
                                handler=item_loop_break, 
                                group=110)                                
    get_workbench().add_command(command_id="item_loop_continue",
                                menu_name=menu_loop["title"][lang_index],
                                command_label=menu_loop["items"][3][lang_index],
                                handler=item_loop_continue, 
                                group=110) 
    menu_func = {
         "title": ["程序和函數", "Procedure", "进程和函数"],
         "items":[
                  ["建立程序", "Procedure declaration", "创建进程"], 
                  ["呼叫程序", "Procedure call", "调用进程"],
                  ["建立函數", "Function declaration", "创建函数"],
                  ["呼叫函數", "Function call", "调用函数"]
                ]
    } 
    # 程序/函數選單
    get_workbench().add_command(command_id="item_sub_def",
                                menu_name=menu_func["title"][lang_index],
                                command_label=menu_func["items"][0][lang_index],
                                handler=item_sub_def, 
                                group=100)                           
    get_workbench().add_command(command_id="item_sub_call",
                                menu_name=menu_func["title"][lang_index],
                                command_label=menu_func["items"][1][lang_index],
                                handler=item_sub_call,
                                group=100)    
    get_workbench().add_command(command_id="item_func_def",
                                menu_name=menu_func["title"][lang_index],
                                command_label=menu_func["items"][2][lang_index],
                                handler=item_func_def, 
                                group=110)                                
    get_workbench().add_command(command_id="item_func_call",
                                menu_name=menu_func["title"][lang_index],
                                command_label=menu_func["items"][3][lang_index],
                                handler=item_func_call, 
                                group=110)                                                  
                                
    menu_turtle = {
         "title": ["Turtle海龜繪圖", "Turtle module", "Turtle 模块"],
         "items":[
                  ["匯入 turtle 模組", "Import turtle module", "导入 turtle 模块"], 
                  ["螢幕暫停顯示圖形", "Screen pause display graphic", "屏幕暂停显示图形"],
                  ["設定視窗尺寸", "Setup window size", "设置窗口尺寸"],
                  ["設定螢幕尺寸", "Setup screen size", "设置屏幕尺寸"],                  
                  ["向前走 x 步", "Move forward x steps", "向前走 x 步"],
                  ["後退走 x 步", "Move backward x steps", "后退走 x 步"],
                  ["向左轉 x 度", "Turn left x degrees", "向左转 x 度"],
                  ["向右轉 x 度", "Turn right x degrees", "向右转 x 度"],                                      
                  ["海龜外觀: 設定海龜色彩", "Turtle look: Set turtle color", "海龟外观: 设置海龟色彩"],
                  ["海龜外觀: 設定海龜圖示", "Turtle look: Set turtle icon", "海龟外观: 设置海龟图标"],
                  ["海龜位置和方向: 走到指定位置", "Turtle position and direction: Go to location", "海龟位置和方向: 走到指定位置"],
                  ["海龜位置和方向: 設定 x 軸位置", "Turtle position and direction: Set X axis position", "海龟位置和方向: 设置 X 轴位置"],
                  ["海龜位置和方向: 設定 y 軸位置", "Turtle position and direction: Set Y axis position", "海龟位置和方向: 设置 Y 轴位置"],      
                  ["海龜位置和方向: 設定海龜方向", "Turtle position and direction: Set turtle direction", "海龟位置和方向: 设置海龟方向"],
                  ["畫筆: 提筆", "Paintbrush: Pen up", "画笔: 提笔"],      
                  ["畫筆: 下筆", "Paintbrush: Pen down", "画笔: 下笔"],
                  ["畫筆: 畫筆寬度", "Paintbrush: Pen Size", "画笔: 画笔宽度"],
                  ["畫筆: 畫筆色彩", "Paintbrush: Pen Color", "画笔: 画笔色彩"],
                  ["填滿色彩: 設定填滿色彩", "Fill color: Set fill color", "填满色彩: 设置填满色彩"],      
                  ["填滿色彩: 開始填滿", "Fill color: Start filling", "填满色彩: 开始填满"],
                  ["填滿色彩: 停止填滿", "Fill color: Stop filling", "填满色彩: 停止填满"]                                
                ]
    }    
    # 海龜繪圖選單
    get_workbench().add_command(command_id="item_turtle_import",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][0][lang_index],
                                handler=item_turtle_import, 
                                group=100)                           
    get_workbench().add_command(command_id="item_turtle_screen_sleep",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][1][lang_index],
                                handler=item_turtle_screen_sleep,
                                group=100) 
    get_workbench().add_command(command_id="item_turtle_windowsize",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][2][lang_index],
                                handler=item_turtle_windowsize, 
                                group=100)                                   
    get_workbench().add_command(command_id="item_turtle_screensize",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][3][lang_index],
                                handler=item_turtle_screensize, 
                                group=100)                                  
    get_workbench().add_command(command_id="item_turtle_forward",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][4][lang_index],
                                handler=item_turtle_forward, 
                                group=105)                                
    get_workbench().add_command(command_id="item_turtle_backward",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][5][lang_index],
                                handler=item_turtle_backward, 
                                group=105)
    get_workbench().add_command(command_id="item_turtle_turnleft",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][6][lang_index],
                                handler=item_turtle_turnleft, 
                                group=105)                                
    get_workbench().add_command(command_id="item_turtle_turnright",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][7][lang_index],
                                handler=item_turtle_turnright, 
                                group=105)                                                             
    get_workbench().add_command(command_id="item_turtle_color",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][8][lang_index],
                                handler=item_turtle_color, 
                                group=110)                                
    get_workbench().add_command(command_id="item_turtle_icon",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][9][lang_index],
                                handler=item_turtle_icon, 
                                group=110)                          
    get_workbench().add_command(command_id="item_turtle_goto",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][10][lang_index],
                                handler=item_turtle_goto, 
                                group=120)                                
    get_workbench().add_command(command_id="item_turtle_setx",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][11][lang_index],
                                handler=item_turtle_setx, 
                                group=120)  
    get_workbench().add_command(command_id="item_turtle_sety",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][12][lang_index],
                                handler=item_turtle_sety, 
                                group=120)                                  
    get_workbench().add_command(command_id="item_turtle_setheading",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][13][lang_index],
                                handler=item_turtle_setheading, 
                                group=120)                                   
    get_workbench().add_command(command_id="item_turtle_penup",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][14][lang_index],
                                handler=item_turtle_penup, 
                                group=130)  
    get_workbench().add_command(command_id="item_turtle_pendown",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][15][lang_index],
                                handler=item_turtle_pendown, 
                                group=130)                                  
    get_workbench().add_command(command_id="item_turtle_pensize",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][16][lang_index],
                                handler=item_turtle_pensize, 
                                group=130)     
    get_workbench().add_command(command_id="item_turtle_pencolor",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][17][lang_index],
                                handler=item_turtle_pencolor, 
                                group=130)                                                                    
    get_workbench().add_command(command_id="item_turtle_fillcolor",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][18][lang_index],
                                handler=item_turtle_fillcolor, 
                                group=140)                                  
    get_workbench().add_command(command_id="item_turtle_begin_fill",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][19][lang_index],
                                handler=item_turtle_begin_fill, 
                                group=140)                                      
    get_workbench().add_command(command_id="item_turtle_end_fill",
                                menu_name=menu_turtle["title"][lang_index],
                                command_label=menu_turtle["items"][20][lang_index],
                                handler=item_turtle_end_fill, 
                                group=140)










    
