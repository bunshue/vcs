# Python 測試 IP power

import sys
import requests

print("------------------------------------------------------------")  # 60個

# To get firmware version : getversion
print('getversion')
url = "http://root:12345678@192.168.2.123/set.cmd?cmd=getversion"
response = requests.get(url)
print(response.text)

# To get MACaddress：getmac
print('getmac')
url = "http://root:12345678@192.168.2.123/set.cmd?cmd=getmac"
response = requests.get(url)
print(response.text)

# To get the status of power on/ off： getpower
print('getpower')
url = "http://root:12345678@192.168.2.123/set.cmd?cmd=getpower"
response = requests.get(url)
print(response.text)

"""
# 上電 setpower&p61=1
url = "http://root:12345678@192.168.2.123/set.cmd?cmd=setpower&p61=1"
response = requests.get(url)
print(response.text)
"""

"""
# 下電 setpower&p61=0
url = "http://root:12345678@192.168.2.123/set.cmd?cmd=setpower&p61=0"
response = requests.get(url)
print(response.text)
"""

"""
# reset, 關了再開 delayTime 2 秒
url = "http://root:12345678@192.168.2.123/set.cmd?cmd=setpowercycle&p61=2"
print('reset')
response = requests.get(url)
print(response.text)
"""

# Get current Amp value : getcurrent
url = "http://root:12345678@192.168.2.123/set.cmd?cmd=getcurrent"
print('getcurrent')
response = requests.get(url)
print(response.text)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

