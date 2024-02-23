# ch15_1.py                 
def greedy(course):
    ''' 課程的貪婪演算法 '''
    length = len(course)                                    # 課程數量
    course_list = []                                        # 儲存結果
    course_list.append(course[0])                           # 第一節課      
    course_end_time = course_list[0][1][1]                  # 第一節課下課時間
    for i in range(1, length):                              # 貪婪選課
        if course[i][1][0] >= course_end_time:              # 上課時間晚於或等於
            course_list.append(course[i])                   # 加入貪婪選課
            course_end_time = course[i][1][1]               # 新的下課時間               
    return course_list
            
course = {'化學':(12, 13),                                  # 定義課程時間
          '英文':(9, 11),
          '數學':(8, 10),
          '計概':(10, 12),
          '物理':(11, 13),
         }

cs = sorted(course.items(), key=lambda item:item[1][1])     # 課程時間排序  
print('所有課程依下課時間排序如下')
print('課程', '   開始時間 ',  ' 下課時間')
for i in range(len(cs)):
    print("{0}{1:7d}:00{2:8d}:00".format(cs[i][0],cs[i][1][0],cs[i][1][1]))

s = greedy(cs)                                              # 呼叫貪婪選課
print('貪婪排課時間如下')
print('課程', '   開始時間 ',  ' 下課時間')
for i in range(len(s)):
    print("{0}{1:7d}:00{2:8d}:00".format(s[i][0],s[i][1][0],s[i][1][1]))
















