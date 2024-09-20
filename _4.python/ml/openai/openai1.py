"""
因為帳號限制 目前應該是不能用了

只是把程式整理在這裡

#pip install openai

"""

print('------------------------------------------------------------')	#60個

import sys
openai_api_key = 'sk-xxxxxxxxx'

#C:\_git\vcs\_1.data\______test_files1\_key

print('------------------------------------------------------------')	#60個

import openai

openai.api_key = openai_api_key  # 設定API金鑰

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "你是一個非常溫暖的對話機器人，回應都簡短，儘量不要超過二十個字，而且有同理心。"},
        {"role": "user", "content": "我很難過"},
        {"role": "assistant", "content": "很抱歉聽到你感到難過，可以跟我說說你正在遭遇什麼困難嗎？我們可以一起找尋解決問題的方式。"},
        {"role": "user", "content": "Python程式都不會寫"}
    ]
)

print(response["choices"][0]["message"]["content"])

print('------------------------------------------------------------')	#60個

import openai

openai.api_key = openai_api_key  # 設定API金鑰

user_input = "Ask ChatGPT something, say hello!"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": user_input}
    ]
)

cc = response.choices[0].message.content
print(cc)

print('------------------------------------------------------------')	#60個

import openai

openai.api_key = openai_api_key  # 設定API金鑰

user_input = "講個笑話來聽聽"

response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=user_input,
    max_tokens=128,
    temperature=0.5,
)

completed_text = response["choices"][0]["text"]
print(completed_text)

print("------------------------------------------------------------")  # 60個

print('AI繪圖')

import openai

openai.api_key = openai_api_key  # 設定API金鑰

user_input = "cat wearing red cape"  #AI繪圖提示詞 DALL-E 2

response = openai.Image.create(
    prompt=user_input,
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)

print('------------------------------------------------------------')	#60個

import openai

openai.api_key = openai_api_key  # 設定API金鑰

# 設定模型和提示語
model_engine = "text-davinci-002"
prompt = "Hi!"

# 設定對話參數
temperature = 0.7
max_tokens = 60
top_p = 1.0

# 定義對話函數
def chat(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
    )
    message = response.choices[0].text.strip()
    return message

print("歡迎來到深智 Deepmind 客服中心")
# 執行對話
while True:
    user_input = input("親愛客戶 : ")
    if user_input == "bye":
        break
    prompt += user_input.strip() + "\n"
    response = chat(prompt)
    print("ChatGPT  : " + response)
    prompt += response + "\n"

print('------------------------------------------------------------')	#60個

print('AI繪圖')

import openai
import urllib.request
from datetime import datetime

openai.api_key = openai_api_key  # 設定API金鑰

user_input = "cat wearing red cape"  #AI繪圖提示詞 DALL-E 2

response = openai.Image.create(
    prompt=user_input,
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)


file_name = "image" + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".png"
urllib.request.urlretrieve(image_url, file_name)

print('------------------------------------------------------------')	#60個

import openai

prompt = "Please generate 10 ideas for coding projects. "

language = "Python"
prompt += "The programming language is " + language + ". "
difficulty = "Easy"
prompt += "The difficulty is " + difficulty + ". "
prompt += "The project should include a database. "
prompt += "The project should include an API."
print(prompt)
    
openai.api_key = openai_api_key  # 設定API金鑰
    
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ]
)
cc = response.choices[0].message.content
print("結果 :", cc)

print('------------------------------------------------------------')	#60個

print('AI繪圖')

import openai
from PIL import Image, ImageTk
import requests, io

openai.api_key = openai_api_key  # 設定API金鑰
user_input = "cat wearing red cape"  #AI繪圖提示詞 DALL-E 2
user_input += "in style: Realistic"

response = openai.Image.create(
    prompt=user_input,
    n=int(number_slider.get()),
    size="512x512"
)

image_urls = []
for i in range(len(response['data'])):
    image_urls.append(response['data'][i]['url'])
print(image_urls)

images = []
for url in image_urls:
    response = requests.get(url)
    image = Image.open(io.BytesIO(response.content))
    photo_image = ImageTk.PhotoImage(image)
    images.append(photo_image)

print('------------------------------------------------------------')	#60個

import openai

openai.api_key = openai_api_key  # 設定API金鑰

"""
做 ChatGPT 方式非常簡單, 就是要用 ChatCompletion, 其中 create 就是正式送給某一個模型。
這裡有兩個重點, 一個是 model 我們要選用的模型, 這裡用的是 gpt-3.5-turbo, 事實上就是 ChatGPT 一開始的標準版本。
然後就是 messages 部份, 這裡就是這次聊天的過程中, 包括我們使用者輸入的, 還有之前 ChatGPT 的回應。
可以看以下內容。後面的 content 比較容易理解, 那 role (角色) 是什麼意思呢? 我們來說明一下:
    system: 給 ChatGPT 的「人設」。
    user: 使用者輸入的東西。
    assistant: ChatGPT 的回應。
"""
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "你是一個非常溫暖的對話機器人，回應都簡短，儘量不要超過二十個字，而且有同理心。"},
        {"role": "user", "content": "我很難過"},
        {"role": "assistant", "content": "很抱歉聽到你感到難過，可以跟我說說你正在遭遇什麼困難嗎？我們可以一起找尋解決問題的方式。"},
        {"role": "user", "content": "Python程式都不會寫"}
    ]
)

#再來就是看我們怎麼讀出 ChatGPT 的回應。

print(response["choices"][0]["message"]["content"])

#3. 打造可以一直聊下去的 ChatGPT!

messages = [{"role": "system", "content": "你是一個非常溫暖的對話機器人，回應都簡短，儘量不要超過二十個字，而且有同理心。"}]

while True:
    prompt = input('> ')
    if 'bye' in prompt:
        print('再見, 下次再聊!')
        break

    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)

    reply = response['choices'][0]['message']["content"]
    print(chatbot + reply)
    print()
    messages.append({"role": "assistant", "content": reply})

print('------------------------------------------------------------')	#60個

import openai

openai.api_key = openai_api_key  # 設定API金鑰

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

print("------------------------------------------------------------")  # 60個

import openai

openai.api_key = openai_api_key  # 設定API金鑰

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

print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

