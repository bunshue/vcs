





"""
#pip install openai

import openai

#C:\_git\vcs\_1.data\______test_files1\_key

openai.api_key = 'sk-xxxxxxxxx'

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "你是一個非常溫暖的對話機器人，回應都簡短，儘量不要超過二十個字，而且有同理心。"},
        {"role": "user", "content": "我很難過"},
        {"role": "assistant", "content": "很抱歉聽到你感到難過，可以跟我說說你正在遭遇什麼困難嗎？我們可以一起找尋解決問題的方式。"},
        {"role": "user", "content": "Python程式都不會寫"}
    ]
)

print('------------------------')
print(response["choices"][0]["message"]["content"])

"""

print('------------------------------------------------------------')	#60個


"""
import openai
import os

# 設定API金鑰
openai.api_key = "OPENAI_API_KEY"

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
"""


"""

print('------------------------------------------------------------')	#60個


import os
import openai  # pip install openai


openai.api_key = os.getenv("OPENAI_API_KEY")

user_prompt = "cat wearing red cape"

response = openai.Image.create(
    prompt=user_prompt,
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)


print('------------------------------------------------------------')	#60個


import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

user_input = input("Enter your prompt for ChatGPT: ")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": user_input}
    ]
)

print(response.choices[0].message.content)



print('------------------------------------------------------------')	#60個


import os
import openai  # pip install openai
import urllib.request
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

user_prompt = input("Write your prompt for DALL-E 2: ")

response = openai.Image.create(
    prompt=user_prompt,
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)


file_name = "image" + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".png"
urllib.request.urlretrieve(image_url, file_name)


print('------------------------------------------------------------')	#60個


import os
import openai # pip install openai
import customtkinter as ctk # pip install customtkinter

def generate():
    prompt = "Please generate 10 ideas for coding projects. "
    language = language_dropdown.get()
    prompt += "The programming language is " + language + ". "
    difficulty = difficulty_value.get()
    prompt += "The difficulty is " + difficulty + ". "
    
    if checkbox1.get():
        prompt += "The project should include a database. "
    if checkbox2.get():
        prompt += "The project should include an API."
    
    print(prompt)
    
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    answer = response.choices[0].message.content
    print(answer)
    result.insert("0.0", answer)

root = ctk.CTk()
root.geometry("750x550")
root.title("ChatGPT Project Idea Generator")

ctk.set_appearance_mode("dark")

title_label = ctk.CTkLabel(root, text="Project Idea Generator", 
                           font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40, 20))

frame = ctk.CTkFrame(root)
frame.pack(fill="x", padx=100)

language_frame = ctk.CTkFrame(frame)
language_frame.pack(padx=100, pady=(20, 5), fill="both")
language_label = ctk.CTkLabel(
    language_frame, text="Programming Language", font=ctk.CTkFont(weight="bold"))
language_label.pack()
language_dropdown = ctk.CTkComboBox(
    language_frame, values=["Python", "Java", "C++", "JavaScript", "Golang"])
language_dropdown.pack(pady=10)

difficulty_frame = ctk.CTkFrame(frame)
difficulty_frame.pack(padx=100, pady=5, fill="both")
difficulty_label = ctk.CTkLabel(
    difficulty_frame, text="Project Difficulty", font=ctk.CTkFont(weight="bold"))
difficulty_label.pack()
difficulty_value = ctk.StringVar(value="Easy")
radiobutton1 = ctk.CTkRadioButton(
    difficulty_frame, text="Easy", variable=difficulty_value, value="Easy")
radiobutton1.pack(side="left", padx=(20, 10), pady=10)
radiobutton2 = ctk.CTkRadioButton(
    difficulty_frame, text="Medium", variable=difficulty_value, value="Medium")
radiobutton2.pack(side="left", padx=10, pady=10)
radiobutton3 = ctk.CTkRadioButton(
    difficulty_frame, text="Hard", variable=difficulty_value, value="Hard")
radiobutton3.pack(side="left", padx=10, pady=10)

features_frame = ctk.CTkFrame(frame)
features_frame.pack(padx=100, pady=5, fill="both")
features_label = ctk.CTkLabel(
    features_frame, text="Features", font=ctk.CTkFont(weight="bold"))
features_label.pack()
checkbox1 = ctk.CTkCheckBox(features_frame, text="Database")
checkbox1.pack(side="left", padx=50, pady=10)
checkbox2 = ctk.CTkCheckBox(features_frame, text="API")
checkbox2.pack(side="left", padx=50, pady=10)

button = ctk.CTkButton(frame, text="Generate Ideas", command=generate)
button.pack(padx=100, fill="x", pady=(5, 20))

result = ctk.CTkTextbox(root, font=ctk.CTkFont(size=15))
result.pack(pady=10, fill="x", padx=100)


root.mainloop()



print('------------------------------------------------------------')	#60個

import os
import openai # pip install openai

openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hi ChatGPT. Say hi back!"}
    ]
)
answer = response.choices[0].message.content
print(answer)

"""

print('------------------------------------------------------------')	#60個

import openai

openai.api_key = "你的 OpenAI API 金鑰"

"""
做 ChatGPT 方式非常簡單, 就是要用 ChatCompletion, 其中 create 就是正式送給某一個模型。
這裡有兩個重點, 一個是 model 我們要選用的模型, 這裡用的是 gpt-3.5-turbo, 事實上就是 ChatGPT 一開始的標準版本。
然後就是 messages 部份, 這裡就是這次聊天的過程中, 包括我們使用者輸入的, 還有之前 ChatGPT 的回應。
可以看以下內容。後面的 content 比較容易理解, 那 role (角色) 是什麼意思呢? 我們來說明一下:
    system: 給 ChatGPT 的「人設」。
    user: 使用者輸入的東西。
    assistant: ChatGPT 的回應。
"""

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


"""

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



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個





