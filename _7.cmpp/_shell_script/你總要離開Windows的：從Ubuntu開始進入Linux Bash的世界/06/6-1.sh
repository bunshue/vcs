#範例指令稿6-1.sh空檔案/dev/null的使用
#! /bin/bash

echo 檢視空檔案/dev/null的內容
cat /dev/null
echo

echo 向檔案中寫入資料
echo 6-1.sh > /dev/null

echo 寫入資料後，檢視檔案的內容
cat /dev/null
