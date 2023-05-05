# 天氣小助理

import requests
import json

def get_cwb_key():
    filename = 'C:/_git/vcs/_1.data/______test_files1/_key/cwb_key.txt'

    import os
    filename=os.path.abspath(filename)
    if not os.path.exists(filename): #檢查檔案是否存在
        print('CWB_KEY 檔案不存在, 離開, 檔案 : ' + filename)
        return ""

    print("讀取檔案 : " + filename)
    fo = open(filename, 'r')
    cwb_key = fo.read()
    fo.close()

    length = len(cwb_key)
    if length != 40:
        print('CWB_KEY 錯誤, 離開')
        return ""
    return cwb_key

def get_data():
    cwb_key = get_cwb_key()
    length = len(cwb_key)
    if length != 40:
        print('CWB_KEY 錯誤, 離開')
        return ""

    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001"
    params = {
        "Authorization": cwb_key,
        "locationName": "新竹市",
    }

    response = requests.get(url, params=params)
    #print(response.status_code)

    if response.status_code == 200:
        # print(response.text)
        data = json.loads(response.text)

        location = data["records"]["location"][0]["locationName"]

        weather_elements = data["records"]["location"][0]["weatherElement"]
        start_time = weather_elements[0]["time"][0]["startTime"]
        end_time = weather_elements[0]["time"][0]["endTime"]
        weather_state = weather_elements[0]["time"][0]["parameter"]["parameterName"]
        rain_prob = weather_elements[1]["time"][0]["parameter"]["parameterName"]
        min_tem = weather_elements[2]["time"][0]["parameter"]["parameterName"]
        comfort = weather_elements[3]["time"][0]["parameter"]["parameterName"]
        max_tem = weather_elements[4]["time"][0]["parameter"]["parameterName"]

        '''
        print('地點 : ')
        print(location)
        print('預測時間啟始 : ')
        print(start_time)
        print('預測時間結束 : ')
        print(end_time)
        print('天氣現象 : ')
        print(weather_state)
        print('降雨機率 : ')
        print(rain_prob)
        print('最低溫度 : ')
        print(min_tem)
        print('最高溫度 : ')
        print(max_tem)
        print('舒適度 : ')
        print(comfort)
        '''

        line_notify(tuple([location, start_time, end_time, weather_state, rain_prob, min_tem, comfort, max_tem]))

    else:
        print("Can't get data!")
        line_notify(tuple())


def get_line_key():
    filename = 'C:/_git/vcs/_1.data/______test_files1/_key/line_key.txt'

    import os
    filename=os.path.abspath(filename)
    if not os.path.exists(filename): #檢查檔案是否存在
        print('LINE_KEY 檔案不存在, 離開, 檔案 : ' + filename)
        return ""

    print("讀取檔案 : " + filename)
    fo = open(filename, 'r')
    line_key = fo.read()
    fo.close()

    length = len(line_key)
    if length != 43:
        print('LINE_KEY 錯誤, 離開')
        return ""
    return line_key

def line_notify(data):
    line_key = get_line_key()
    length = len(line_key)
    if length != 43:
        print('LINE_KEY 錯誤, 離開')
        return ""

    token = line_key
    message = ""

    if len(data) == 0:
        message += "\n[Error] 無法取得天氣資訊"
    else:
        message += f"\n今天{data[0]}的天氣: {data[3]}\n"
        message += f"溫度: {data[5]}°C - {data[7]}°C\n"
        message += f"降雨機率: {data[4]}%\n"
        message += f"舒適度: {data[6]}\n"

        if int(data[4]) > 70:
            message += "提醒您，今天很有可能會下雨，出門記得帶把傘哦!\n"
        elif int(data[7]) > 33:
            message += "提醒您，今天很熱，外出要小心中暑哦~\n"
        elif int(data[5]) < 10:
            message += "提醒您，今天很冷，記得穿暖一點再出門哦~\n"

        message += f"時間: {data[1]} ~ {data[2]}"

    # line notify所需資料
    line_url = "https://notify-api.line.me/api/notify"
    line_header = {
        "Authorization": 'Bearer ' + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    line_data = {
        "message": message
    }

    x = requests.post(url=line_url, headers=line_header, data=line_data)
    #print(x.status_code)


if __name__ == '__main__':
    # line_notify(tuple(["台南市", "2021-08-31", "2021-09-01", "晴", "10", "20", "舒適", "25"]))
    get_data()
