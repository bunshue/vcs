#範例指令稿9-11.sh  陣列作為函數傳回值
#!/bin/bash

fun()
{
        local old
        local new
        local num
        local i
        old=(`echo "$@"`)
        new=(`echo "$@"`)
        num=$[ $# - 1 ]
echo 傳遞給函數的陣列為：${old[*]}"

        for (( i = 0; i <= $num; i++ ))
        {
new[$i]=$[ ${old[$i]} * 2 ]
        }
        echo ${new[*]}
}
array=(1 2 3 4 5)
echo "陣列的值為: ${array[*]}"
arg1=`echo ${array[*]}`
result=(`fun $arg1`) 
echo "函數的傳回陣列為: ${result[*]}"
