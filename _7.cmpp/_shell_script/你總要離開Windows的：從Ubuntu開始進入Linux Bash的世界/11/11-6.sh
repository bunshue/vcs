#範例指令稿11-6.sh  使用*比對字元
 #！ /bin/bash

echo 顯示包括11的所有檔案
ls -l  *11*
echo

echo 顯示以11開頭的檔案
ls -l 11*
echo

echo顯示以11結尾的檔案
ls -l *11
