# ch38_2.py
import openai

# 設定API金鑰 
openai.api_key = 'Your_API_Key'

# 定義對話函數
def chat(messages):
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = messages,
        max_tokens = 150     # 限制回應token數
    )
    return response.choices[0].message['content']

print("歡迎使用Emoji Translation工具")

# 初始化對話串列
messages = [{"role": "system", "content": "你是emoji翻譯專家"}]

# 執行對話
while True:
    user_input = input("請輸入要翻譯的文字 : ")
    if user_input.lower() == "bye":
        print("Emoji翻譯專家 : 感謝您的使用，再見！👋")
        break
    # 將用戶輸入的文字構建為帶有翻譯要求的問句
    translation_request = f"翻譯下列文字為emojis: '{user_input}'"
    messages.append({"role": "user", "content": translation_request})
    response = chat(messages)
    print("Emoji翻譯專家  : " + response)
    messages.append({"role": "assistant", "content": response})


