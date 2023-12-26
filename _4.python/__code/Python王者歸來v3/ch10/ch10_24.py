# ch10_24.py
# students是學生名單集合
students = {'Peter', 'Norton', 'Kevin', 'Mary', 'John',     
            'Ford', 'Nelson', 'Damon', 'Ivan', 'Tom'
           }

Math = {'Peter', 'Kevin', 'Damon'}          # 數學夏令營參加人員
Physics = {'Nelson', 'Damon', 'Tom' }       # 物理夏令營參加人員

MorP = Math | Physics
print("有 %d 人參加數學或物理夏令營名單  : " % len(MorP), MorP )
unAttend = students - MorP
print("沒有參加任何夏令營有 %d 人名單是 : " % len(unAttend), unAttend)












