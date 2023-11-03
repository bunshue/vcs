#範例指令稿7-16.sh  case結構的使用
#! /bin/bash

echo 目前使用的使用者為$USERNAME
echo 使用case結構
case $USERNAME in 
"root") echo 使用root使用者登入，具有最高權限;;
"ben") echo 使用ben使用者登入，具有普通權限;;
*) echo 使用其他使用者登入，具有權限不明確;;
esac
echo 結束case結構
