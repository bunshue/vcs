#範例指令稿17-11.sh  網路基本組態，組態IP位址、子網遮罩、預設通訊閘和路由訊息
#! /bin/bash

echo 使用ifconfig指令進行網路設定
ifconfig  eth0 192.168.1.1
ifocnfig eth0 netmask 255.255.255.0
route add default gw 192.168.1.1

echo 顯示最新的網路組態
ifconfig
