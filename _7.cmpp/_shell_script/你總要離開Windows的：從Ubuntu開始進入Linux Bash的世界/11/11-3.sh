#範例指令稿11-3.sh 查詢開頭字元為脫字元
#!/bin/bash

#^
echo比對開頭字元為脫字元
grep   "#\^" 11-3.sh
echo

echo 查詢包括脫字元的文字行
grep   "*#\^*" 11-3.sh
