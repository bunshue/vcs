#範例指令稿4-10.sh  使用-e選項輸出特殊字元
#! /bin/bash

echo -e warning:\a
echo -e \"this is shell script\"
echo "插入反斜槓"
echo -e  this \\is
