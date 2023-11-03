#範例指令稿6-5.sh連結檔案的使用
#! /bin/bash
mv  6-2.sh test.sh
ln test.sh HLtest #file為原檔名，filenew為新檔名。 #建立硬軟連結指令
ls -l #顯示檔案屬性

ln -s test.sh SLtest  #file為原檔名，filenew為新檔名 # 建立軟連結指令 
ls -l #顯示檔案屬性

rm test.sh
cat HLtest SLtest
