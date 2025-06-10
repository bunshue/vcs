from machine import ADC
import urequests as req
import network,time

SSID='自己的SSID'
PASSWORD='自己的密碼'
def do_connect():
    sta = network.WLAN(network.STA_IF) # Station
    if not sta.isconnected():
        print('正在連線中...')
        sta.active(True) #啟用 STA 模式
        sta.connect(SSID, PASSWORD) #連線基地台
        # 等侯連線
        while not sta.isconnected():
            pass
    print('連線成功!')
              
do_connect() # Connect to network

A0 = ADC(0)

host='https://api.thingspeak.com'       
api_key='0O6HE9KF3DR1W1DV'   # Write Key (光線感測器)

def sendData():    
    try:    
        value = A0.read() # 讀取 A0 埠
    except OSError as e:
        print(e)
        return
  
    apiURL='%s/update?api_key=%s&field1=%s' %(host, api_key, value) 
    print(apiURL)

    r = req.get(apiURL)
    if r.status_code == 200:
        print('第 {} 筆資料傳送成功!' .format(r.text))
    else:
        print('資料傳送錯誤!')  

try:
    while True:
        sendData()
        time.sleep(20)        
except:
    print('結束執行')