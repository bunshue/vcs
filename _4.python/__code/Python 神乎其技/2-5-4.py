# 2-5-4 樣板字串格式化

from string import Template

errno = 50159747054
name = '鮑勃'

templ_string = '嘿 $name, 有錯誤 $error 發生了!'
print(Template(templ_string).substitute(name=name, error=hex(errno)))