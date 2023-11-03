#範例指令稿11-2.sh  點字元比對單字元
#!/bin/bash

#Hello
#123HEllo
#123hEllo
echo "顯示開頭是#1的"
grep [^1] 11-2.sh
echo
echo 顯示開頭是H的
