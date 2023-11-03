#範例指令稿11-1.sh  點字元比對單字元
#!/bin/bash

#Hello
#HEllo
#hEllo
echo 使用點字元比對字元
grep  -v H.llo 11-1.sh 
echo

grep ..llo 11-1.sh
