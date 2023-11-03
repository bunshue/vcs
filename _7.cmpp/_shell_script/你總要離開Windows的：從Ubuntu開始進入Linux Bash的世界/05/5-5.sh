#範例指令稿5-5.sh 通配符星號？的使用
#! /bin/bash

echo 使用通配符星號\"?\"
mkdir file filE FilE File 

echo 比對第一個字元
ls ?ile

echo 比對第後一個字元
ls fil?

echo 多個通配符共同使用
ls ?i*
