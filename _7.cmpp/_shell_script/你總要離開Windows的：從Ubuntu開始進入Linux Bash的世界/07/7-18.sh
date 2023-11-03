#範例指令稿7-18.sh  select指令的使用案例
#! /bin/bash
echo select指令的使用
select choose in 雞 鴨 魚 肉 其他
do
break
done
echo  你喜歡的是$choose
