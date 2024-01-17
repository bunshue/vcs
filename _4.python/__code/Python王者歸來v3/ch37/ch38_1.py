# ch38_1.py
import openai

# 設定API金鑰
openai.api_key = 'Your_API_Key'

# 定義對話函數
def chat(messages):
    response = openai.ChatCompletion.create(
        model = "gpt-4",
        messages = messages,
        max_tokens = 150            # 限制回應token數
    )
    return response.choices[0].message['content']

print("歡迎來到深智 Deepwisdom 客服中心")

# 初始化對話串列
messages = [{"role": "system", "content": "你是深智公司客服人員"}]

# 執行對話
while True:
    user_input = input("    客戶 : ")
    if user_input.lower() == "bye":
        print("深智客服 : 感謝您的諮詢，祝您有美好的一天！")
        break
    messages.append({"role": "user", "content": user_input})
    response = chat(messages)
    print("深智客服 : " + response)
    messages.append({"role": "assistant", "content": response})



