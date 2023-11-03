#範例指令稿12-7.sh  grep檢索多個關鍵字
#! /bin/bash
#hello
#Hello
#HELLO
#HEllo
#HELlo

echo '使用grep指令的-E選項'
echo '比對hello|Hello'
grep -E "hello|Hello" 12-7.sh
echo
echo '比對HE.lo|hello'
grep -E "HE.lo|hello" 12-7.sh
