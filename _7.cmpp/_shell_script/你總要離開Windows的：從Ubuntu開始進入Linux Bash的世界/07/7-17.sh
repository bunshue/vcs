#範例指令稿7-17.sh  使用if結構置換case結構
#! /bin/bash

echo 使用if結構置換case結構
echo 目前使用的使用者為$USERNAME

if [ $user = root ]
then
echo 使用root使用者登入，具有最高權限
	elif [ $user = ben ]
then
echo 使用ben使用者登入，具有普通權限
else
 echo 使用其他使用者登入，具有權限不明確
fi
