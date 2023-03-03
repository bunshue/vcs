# _*_ coding: utf-8 _*_
# 程式 11-6 (Python 3 version)

from firebase import firebase
db_url = 'https://python01.firebaseio.com'
auth = firebase.FirebaseAuthentication('****', 'skynet.tw@gmail.com', 
    extra={'eAuth': 'GX453Q3U7hTqjvtCnSf****BX8Fa8kI3v7f4gWNN'})
fdb = firebase.FirebaseApplication(db_url, auth)

def disp_menu():
    print('統一發票號碼管理')
    print('-------------')
    print('1. 輸入開獎號碼')
    print('2. 顯示開獎號碼')
    print('3. 刪除開獎號碼')
    print('0. 結束程式')
    print('-------------')
    ans = input('您的選擇：')
    return int(ans)

def enter_lotto():
    while True:
        inv_lotto = dict()
        inv_month = input('請輸入開獎月份(例：201511，輸入-1結束):')
        if int(inv_month) == -1 :
            break
        exist_data = fdb.get('/invlotto/'+inv_month, None)
        if exist_data != None:
            print("該月份已有資料，請重新輸入")
            continue
        inv_lotto['p1000w'] = input('請輸入特別獎1000萬號碼：')
        inv_lotto['p200w'] = input('請輸入特獎200萬號碼：')
        inv_lotto['p20w'] = list()
        while True:
            p20w = input('請輸入頭獎20萬號碼（輸入-1結束）：')
            if int(p20w) == -1:
                break
            inv_lotto['p20w'].append(p20w)
        inv_lotto['p200'] = list()
        while True:
            p200 = input('請輸入增開六獎號碼（輸入-1結束)：')
            if int(p200) == -1:
                break
            inv_lotto['p200'].append(p200)
        print("以下是您輸入的內容：")
        print("開獎月份:", inv_month)
        print("1000萬特別獎:", inv_lotto['p1000w'])
        print("200萬特獎:", inv_lotto['p200w'])
        print("20萬頭獎:", end="")
        for n in inv_lotto['p20w']:
            print(n + "  ", end="")
        print("\n200元增開六獎:", end="")
        for n in inv_lotto['p200']:
            print(n + "  ", end="")
        ans = input("\n是否寫入Firebase網路資料庫？(y/n)")
        if ans == 'y' or ans == 'Y':
            fdb.post('/invlotto/' + inv_month, inv_lotto)

def disp_lotto():
    lottos = fdb.get('/invlotto', None)
    if lottos == None:
        print('沒有任何開獎資料可供顯示...')
        return
    inv_months = list(lottos.keys())
    print("現有資料如下：")
    for inv_month in inv_months:
        print("開獎月份：", inv_month)
        key_id = list(lottos[inv_month].keys())[0]
        print("1000萬特別獎：{}".format(lottos[inv_month][key_id]['p1000w']))
        print(" 200萬  特獎：{}".format(lottos[inv_month][key_id]['p200w'])) 
        print("  20萬  頭獎：", end="")
        for i in lottos[inv_month][key_id]['p20w']:
            print(str(i) + "   ", end="")
        print("\n    增開六獎：", end="")
        for i in lottos[inv_month][key_id]['p200']:
            print(str(i) + "   ", end="")
        print("\n")

def del_lotto():
    lottos = fdb.get('/invlotto', None)
    if lottos == None:
        print('沒有任何開獎資料可供刪除...')
        return
    inv_months = list(lottos.keys())
    print("現有可刪除資料如下：")
    for inv_month in inv_months:
        print(inv_month)
    target = input('請輸入欲刪除的月份(-1表示不刪除)：')
    if target not in inv_months:
        print("輸入錯誤，無此月份資料...")
        return

    key_id = list(lottos[target].keys())[0]
    print(lottos[target][key_id])
    ans = input('你確定要刪除以上這份資料嗎？(y/n)')
    if ans == 'y' or ans == 'Y':
        fdb.delete('/invlotto/'+target, None)

while True:
    ans = disp_menu()
    if ans == 1:
        enter_lotto()
    elif ans == 2:
        disp_lotto()
    elif ans == 3:
        del_lotto()
    else:
        break
print("程式結束，謝謝使用")
