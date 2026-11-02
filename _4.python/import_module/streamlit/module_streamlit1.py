"""
#使用 Streamlit 簡單又快速建立 Dashboard 網頁

Streamlit 幫助我們快速製作 Web 應用程式，而且不需要任何前端技能，全部都採用 Python 語法完成。讓你輕鬆分享網路爬蟲、數據科學和機器學習的資料，是一個非常方便的套件。

pip install streamlit

執行
streamlit run <py程式檔案路徑>
指定埠號
streamlit run <py程式檔案路徑> --server.port 8888


需要終止該應用程式只需在終端中按 Ctrl + C
"""

import os
import sys
import time
import random
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個
import time
import numpy as np
import pandas as pd

import streamlit as st

st.title('我的第一個應用程式')

st.write("嘗試創建**表格**：")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
df


print("------------------------------------------------------------")  # 60個

#繪製圖表和地圖 Chart
#折線圖 st.line_chart()

#使用 Numpy 生成一個隨機樣本，然後將其繪製成折線圖。

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)


#地圖 st.map()
#使用 Numpy 生成一個隨機樣本，繪製到地圖上。

map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [22.6, 120.4],
    columns=['lat', 'lon'])
st.map(map_data)

#輸入類元件

#除了上述標題、圖表，還有其他小工具，像是按鈕、選擇框、複選框、滑塊等等。

#按鈕 st.button()

if st.button('不要按!'):
    st.text("不是叫你不要按了嗎！")


#複選框 st.checkbox()
#使用複選框來顯示/隱藏數據，例如將剛剛繪製地圖的程式改成：

if st.checkbox('顯示地圖圖表'):
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [22.6, 120.4],
        columns=['lat', 'lon'])
    st.map(map_data)


#選擇框 st.selectbox()
#使用選擇框提供使用者選擇：

option = st.selectbox(
    '你喜歡哪種動物？',
    ['狗', '貓', '鸚鵡', '天竺鼠'])
st.text(f'你的答案：{option}')

#調整佈局 Layout
#除了剛剛示範的一行一個元件，Streamlit 有提供幾種佈局容器元件供使用、排版。
"""
#側邊欄 st.sidebar
#例如我們能將元件移到側邊欄中，這邊範例將剛剛的選擇框移入側邊欄：

option = st.sidebar.selectbox(
    '你喜歡哪種動物？',
    ['狗', '貓', '鸚鵡', '天竺鼠'])
st.sidebar.text(f'你的答案：{option}')

#列容器 st.columns()
#也有左右兩邊的方式來排列的容器：

left_column, right_column = st.columns(2)
left_column.write("這是左邊欄位。")
right_column.write("這是右邊欄位。")
"""

#展開容器 st.expander()
#也可以通過能展開的容器，來隱藏大量內容來節省空間：

expander = st.expander("點擊來展開...")
expander.write("如果你要顯示很多文字，但又不想佔大半空間，可以使用這種方式。")

#分頁容器 st.tabs()
#或者切出不同分頁，來放置不同種類的資料：

tab1, tab2 = st.tabs(["Cat 介紹", "Dog 介紹"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)


#狀態元件 Status
#進度條 st.progress()
#使用 time.sleep() 來模擬進度條的等待：

bar = st.progress(0)
for i in range(100):
    bar.progress(i + 1, f'目前進度 {i+1} %')
    time.sleep(0.05)

bar.progress(100, '載入完成！')


#而且網頁右上角還會顯示"RUNNING…"，並有多個運動圖示跳動，讓使用者知道目前網頁中還有東西正在運行。
#進度條載入時，網頁右上角 RUNNING... 字樣

#消息通知 st.toast()
#當有時候我們會需要跳出一個消息通知使用者，但並不想太干擾使用者，這時候就可以使用 st.toast()：

#也可以為文字加上顏色，和加上 icon。

if st.button('儲存', type="primary"):
    st.toast(':rainbow[你編輯的內容已經保存]', icon='💾')
    # 或是簡單點，只顯示文字
    # st.toast('你編輯的內容已經保存')


#box 訊息 st.success()、st.info()、st.warning()、st.error()
#或者想要在頁面上顯示較醒目的錯誤訊息：

st.success('Success!')
st.info('Info!')
st.warning('Warning!')
st.error('Error!', icon='🚨')

#特效 st.balloons() 與 st.snow()

#還有看似無用，但真的好像無用(?)的特效，

#慶祝氣球 st.balloons()
st.balloons()
#慶祝降雪 st.snow()
#st.snow()

#聊天元件 Chat
#聊天元件 st.chat_message() 與 st.chat_input()
#最近因為 ChatGPT 之類的 LLM 熱門而新增的 "聊天元件" st.chat_message()、st.chat_input()：

with st.chat_message("user"):  # 或者寫 "human"
    st.write("Hi 👋，請問你是誰？")

# 另一種寫法
message = st.chat_message("assistant")  # 或者寫 "ai"
# message = st.chat_message("assistant", avatar="🦖")  # 自訂頭像
message.write("你好！我是 ChatBot 🤖，可以回答各種問題，提供資訊。")
message.write("有什麼我可以幫助你的嗎？")

st.chat_input("Say something...")


#表單元件
#表單 st.form()

#經過上面的嘗試，我們都發現在 Streamlit 中，操作每個元件都會導致整個應用程式重新運行。
#但是，有時我們可能希望像表單那樣，全部填寫好後再一次觸發(提交)，這時候就可以使用 st.form() 表單元件：

with st.form(key='my_form'):
    form_name = st.text_input(label='姓名', placeholder='請輸入姓名')
    form_gender = st.selectbox('性別', ['男', '女', '其他'])
    form_birthday = st.date_input("生日")
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write(f'hello {form_name}, 性別:{form_gender}, 生日:{form_birthday}')

#使用快取 Caching

#要使用 @st.cache_data 裝飾器，就需要將運算部分的程式碼包成函式(def)。

@st.cache_data(ttl=3600, show_spinner="正在加載資料...")  # 👈 Add the caching decorator
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data("https://raw.githubusercontent.com/plotly/datasets/master/26k-consumer-complaints.csv")
st.dataframe(df)

#第一次載入時會跑比較久(上面範例是讓它到網路上下載 csv 資料後顯示)，之後再重整網頁時，因為有快取的關係，它應該一瞬間就顯示出來了。

#如果想要清除快取再測試，可以從右上角的選單選擇 "Clear caches"：
#右上角選單 "Clear caches" 可以清除快取

"""
#網頁配置設定
#網頁配置程式碼要寫在所有 Streamlit 命令之前，而且只能設定一次。

此函式有五個參數：

    page_title：網頁標題，顯示在瀏覽器分頁的標籤上，預設是程式碼的檔名。
    page_icon：網頁圖標，顯示在網頁標題前，可以使用 st.image 或 Emoji，或者使用"random"讓它隨機產生XD。
    layout：網頁中佈局寬度，預設是"centered"，還可以使用"wide"。
    initial_sidebar_state：側邊欄顯示狀態，"expanded"打開或"collapsed"隱藏，預設是"auto"，代表在手機尺寸的設備上是隱藏，否則是打開顯示。
    menu_items：右上角的菜單設定，共有以下三項可以設定：
        “Get help”：設定 URL，如果沒有，則會隱藏此菜單選項。
        “Report a Bug”：設定 URL，如果沒有，則會隱藏此菜單選項。
        “About”：顯示在 "關於" 彈跳視窗中的 Markdown 字串，如果沒有，則僅顯示 Streamlit 預設的內容。
        URL 也可以設定為電子郵件地址，像是 mailto:john@example.com。

st.set_page_config(
   page_title="自定義網頁標題",
   page_icon="random",
   layout="centered",
   initial_sidebar_state="expanded",
   menu_items={
        'Get Help': 'https://blog.jiatool.com/about/',
        'About': "# 這是什麼網頁？ \n**[IT空間](https://blog.jiatool.com/)** 示範 streamlit 之用網頁"
    }
)
"""

"""
部署應用程式

除了將程式在自己的電腦執行，或架在伺服器之外，官方有提供「Streamlit Community Cloud」，可以在上面部署、管理、共享你的 Streamlit 應用程式。你只要將專案上傳自己的 GitHub 存儲庫(公開或私有都可以)，再到 Streamlit Community Cloud 設定連接即可，算是蠻方便的。

* 關於 Streamlit Community Cloud 官方說明可在這邊查看：Welcome to Streamlit Community Cloud

完整部署介紹請參考官方說明，只需要四個步驟：

    先確認你的資料夾內有程式執行需要的依賴套件文件：
        Python 依賴文件 [必要]：requirements.txt、Pipfile、environment.yml、pyproject.toml 這幾種擇一，指定程式需要哪些 Python 套件。
        apt-get 依賴 [非必要]：需要哪些 apt-get 的依賴套件。
    將專案推到自己的 GitHub (公開或私有都可以)。
    前往 share.streamlit.io 工作區，連接你剛剛上傳的 GitHub 存儲庫。
    部署完成！！


推上 GitHub 的專案資料夾內大致會長這樣：

your-repository/
├── streamlit_app.py
└── requirements.txt

推上 GitHub Repository
推上 GitHub Repository

前往 share.streamlit.io 工作區，連接你剛剛上傳的 GitHub 存儲庫。

點擊右上角 "New app"
右上角 "New app"
右上角 "New app"

第一次需要給 Streamlit 擁有讀取 GitHub Repository 的權限：
第一次需要給 Streamlit 讀取 GitHub 權限
第一次需要給 Streamlit 讀取 GitHub 權限

下一步，指定 GitHub Repository、分支、程式檔案名稱，以及是否要自訂網址名稱(你可以為你的應用程式自訂一個獨一無二的名稱)：
部署設定
部署設定

下方還可以打開 "Advanced settings…"，這邊可以更改 Python 版本、設定環境變數。
我們這個範例不需要編輯這邊。
部署進階設定
部署進階設定

點擊 "Deploy!"，等個一、兩分鐘安裝。
部署中...
部署中...

部署完成，網址列上顯示的就是你這個應用程式的專屬網址，把它分享給其他人炫耀你努力的成果吧~🎉
部署完成
部署完成


前往 share.streamlit.io 工作區，可以查看你全部的 Streamlit 應用程式，它還提供統計來訪人數的功能。
share.streamlit.io 工作區
share.streamlit.io 工作區

來看看我 2021 年發布的 Demo 範例，共有 1,522 名讀者來訪~ (而且是計算不重複的)
* 這個統計功能是從 2022 年 4 月才開始，所以實際上會再更多。
統計來訪人數
統計來訪人數

完整範例程式碼

附上完整範例程式碼：streamlit_app.py

此範例程式碼部署在 Streamlit Cloud (share.streamlit.io) 的 Demo：
Streamlit 成果範例：streamlit_2023_demo

結語

從之前第一次嘗試 Streamlit 到現在過了兩年多，它又陸續新增了不少功能，看起來還有積極再發展。

經過上方教學實際操作後，會發覺這個套件真的可以很簡單、快速的建立一個顯示資料用的儀表板(Dashboard)，因此特別寫這篇文章來分享給大家~


參考：
Streamlit 官方網站
Streamlit 官方文檔
"""

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

