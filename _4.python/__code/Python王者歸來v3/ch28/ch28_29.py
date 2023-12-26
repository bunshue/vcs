# ch28_29.py
import pyautogui
import time

# 給予一些時間來切換到瀏覽器視窗
time.sleep(5)

# 假設的表單填寫
# 移動到名字輸入框的位置並按一下, 需要根據實際位置調整座標
pyautogui.click(x=200, y=300)       # 這裡的 x 和 y 值需要您自己設定
pyautogui.write('John Doe', interval=0.1)

# 移動到郵件欄位輸入框的位置
pyautogui.click(x=200, y=350)       # 這裡的 x 和 y 值需要您自己設定
pyautogui.write('cshung@example.com', interval=0.1)

# 如果有更多欄位, 重複上述步驟

# 最後移動到提交按鈕並按一下
pyautogui.click(x=200, y=400)       # 這裡的 x 和 y 值需要您自己設定


