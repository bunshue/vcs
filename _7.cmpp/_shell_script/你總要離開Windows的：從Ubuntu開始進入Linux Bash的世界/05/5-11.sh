#範例指令稿5-11.sh 括號的使用
#! /bin/bash

 echo "請輸入登入使用者的姓名:"
read name
echo 不使用括號
echo  歡迎$name的登入
echo 使用括號
echo歡迎${name}的登入
