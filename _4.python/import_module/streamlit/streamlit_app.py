import time
import streamlit as st
import numpy as np
import pandas as pd


st.set_page_config(
   page_title="IT空間 示範 streamlit",
   page_icon="🎉",
   layout="centered",
   initial_sidebar_state="expanded",
   menu_items={
        'Get Help': 'https://blog.jiatool.com/about/',
        'About': "# 這是什麼網頁？ \n**[IT空間](https://blog.jiatool.com/)** 示範 streamlit 之用網頁"
    }
)


st.title('我的第一個應用程式')

st.subheader('兩種最簡單的寫法')

st.write("嘗試創建**表格**：")
# 會自動判斷並轉換成 markdown
# st.markdown('嘗試創建**表格**：')

df = pd.DataFrame({
    '第一個欄位': ['a', 'b', 'c'],
    '第二個欄位': [10, 20, 30]
})
df


st.subheader('繪製圖表和地圖')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)
st.bar_chart(chart_data, color=['#8ECDDD', '#4F709C', '#E5D283'])
# 還可以使用滑鼠縮放和移動


st.subheader('按鈕/開關元件')

if st.checkbox('顯示地圖圖表'):
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [22.6, 120.4],
        columns=['lat', 'lon'])
    st.map(map_data)


# 放到側邊欄
option = st.sidebar.selectbox(
    '你喜歡哪種動物？',
    ['狗', '貓', '鸚鵡', '天竺鼠'])
st.sidebar.text(f'你的答案：{option}')

st.sidebar.text_input("你的姓名 (要按\"Enter\"才算確認輸入)", key="name")
if st.session_state.name != "":
    st.sidebar.text(f'你好, "{st.session_state.name}"~')  # 使用 text_input 的 key 取取得使用者輸入的資料


st.divider()

# 左右排列
left_column, right_column = st.columns(2)

# 您可以使用像 st.sidebar 一樣的列
left_column.multiselect('喜好', ['運動', '閱讀', '電腦/手機遊戲', '繪畫', '樂器'])
if left_column.toggle('開/關'):
    left_column.write('你開啟了開關')

# 或者更好的是，在“with”塊內調用 Streamlit 函數：
with right_column:
    chosen = st.radio('你住在哪裡？', ("地球", "月亮", "火星"))
    st.write(f"我是 {chosen} 人！！")


st.subheader('狀態類元件')
col1, col2 = st.columns(2)

with col1:
    if st.button('不要按!'):
        st.text("不是叫你不要按了嗎！")
    if st.button('氣球特效'):
        st.balloons()
    if st.button('下雪特效'):
        st.snow()
    if st.button('右下角跳出一則消息', type="primary"):
        st.toast(':rainbow[你編輯的內容已經保存]', icon='💾')

with col2:
    st.success('Success!')
    st.info('Info!')
    st.warning('Warning!')
    st.error('Error!', icon='🚨')


st.subheader('表單元件')

with st.form(key='my_form'):
    form_name = st.text_input(label='姓名', placeholder='請輸入姓名')
    form_gender = st.selectbox('性別', ['男', '女', '其他'])
    form_birthday = st.date_input("您的生日")
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write(f'hello {form_name}, 性別:{form_gender}, 生日:{form_birthday}')


# 隱藏大量內容來節省空間
with st.expander("點擊來展開 \"媒體元件\" ..."):
    # 選項卡(tab)
    tab1, tab2, tab3 = st.tabs(["圖片", "音樂", "影片"])
    tab1.image("https://images.unsplash.com/photo-1548407260-da850faa41e3", caption='Sunrise by the mountains')
    tab2.audio('https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg', format='audio/ogg')
    tab3.video("https://www.youtube.com/watch?v=D6DVTLvOupE", start_time=60)


with st.expander("使用快取功能來避免重複載入..."):
    @st.cache_data(ttl=180, show_spinner="正在加載資料...")  # Time to Live
    def expensive_computation(a):
        st.write(f"沒有快取：expensive_computation({a})")
        time.sleep(2)
        return a * a

    num = st.slider("選擇一個數字", 0, 10)
    result = expensive_computation(num)
    st.write("結果：", result)


with st.expander("最近因為 ChatGPT 熱門而新增的\"聊天元件\"..."):
    with st.chat_message("user"):  # 或者寫 "human"
        st.write("Hi 👋")
        st.write("請畫出一張面積圖表")

    message = st.chat_message("assistant")  # 或者寫 "ai"
    # message = st.chat_message("assistant", avatar="🦖")  # 自訂頭像
    message.write("Hello human, 當然沒問題~")
    message.area_chart(pd.DataFrame(np.random.randn(20, 2)))


if st.button('開始展示進度條'):
    progress_text = "載入中，請稍後..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1, text=progress_text)
    my_bar.progress(100, text="載入完成！")


# 更多其他元件請參考官方說明：https://cheat-sheet.streamlit.app/ 或 API文件 https://docs.streamlit.io/library/api-reference
# st.header('My header')
# st.subheader('My sub')
# st.markdown('_Markdown_')
# st.latex(r''' e^{i\pi} + 1 = 0 ''')
# st.code('for i in range(8):\n    foo()')
# st.metric(label="Temperature", value="32 °C", delta="1.2 °C")

# st.multiselect('Multiselect', [1, 2, 3])
# start_color, end_color = st.select_slider(
#     'Select a range of color wavelength',
#     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
#     value=('red', 'blue'))
# st.number_input('Enter a number')
# st.text_area('Area for textual entry')
# st.date_input('Date input')
# st.time_input('Time entry')
# st.file_uploader("選擇一個檔案", type=['png', 'jpg'], help="可以加上更詳細的說明文字。")
# st.color_picker('Pick a color')
