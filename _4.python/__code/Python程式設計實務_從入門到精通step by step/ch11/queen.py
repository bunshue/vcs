global queen
global number
EIGHT=8 #定義最大堆疊容量
queen=[None]*8 #存放8個皇后之列位置

number=0#計算總共有幾組解的總數
#決定皇后存放的位置
#輸出所需要的結果
def print_table():
    global number
    x=y=0
    number+=1
    print('')
    print('八皇后問題的第%d組解\t' %number)
    for x in range(EIGHT):
        for y in range(EIGHT):
            if x==queen[y]:
                print('<q>',end='')
            else:
                print('<->',end='')
        print('\t')
    input('\n..按下任意鍵繼續..\n')

#測試在(row,col)上的皇后是否遭受攻擊
#若遭受攻擊則傳回值為1,否則傳回0
def attack(row,col):
    global queen
    i=0
    atk=0
    offset_row=offset_col=0
    while (atk!=1)and i<col:
        offset_col=abs(i-col)
        offset_row=abs(queen[i]-row)
        #判斷兩皇后是否在同一列在同一對角線上
        if queen[i]==row or offset_row==offset_col:
            atk=1
        i=i+1
    return atk

def decide_position(value):
    global queen
    i=0
    while i<EIGHT:
        if attack(i,value)!=1:
            queen[value]=i
            if value==7:
                print_table()
            else:
                decide_position(value+1)
        i=i+1

#主程式
decide_position(0)
