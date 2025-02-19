import requests
import xml.etree.cElementTree as ET

def showCurrent():
    try:
        content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
        tree = ET.fromstring(content.text)  #解析XML
        items = list(tree.iter(tag='item'))  #取得item標籤內容
        print('期別0 :', items[0][0].text)
        print('網址0 :', items[0][1].text)
        print('時間0 :', items[0][2].text)
        print('號碼0 :', items[0][3].text)
        print('期別1 :', items[1][0].text)
        print('網址1 :', items[1][1].text)
        print('時間1 :', items[1][2].text)
        print('號碼1 :', items[1][3].text)
        print('期別2 :', items[2][0].text)
        print('網址2 :', items[2][1].text)
        print('時間2 :', items[2][2].text)
        print('號碼2 :', items[2][3].text)
        print('期別3 :', items[3][0].text)
        print('網址3 :', items[3][1].text)
        print('時間3 :', items[3][2].text)
        print('號碼3 :', items[3][3].text)
        
        title = items[0][0].text  #期別
        print('期別 :', title)
        ptext = items[0][3].text  #中獎號碼
        print('號碼 :', ptext)
        ptext = ptext.replace('<p>','').replace('</p>','\n')
        message = title + '月\n' + ptext[:-1]  #ptext[:-1]為移除最後一個\n
        print('message :', message)
        print('號碼 :', ptext)
    except:
        print('讀取發票號碼發生錯誤！')

def showOld():
    try:
        content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
        tree = ET.fromstring(content.text)  #解析XML
        items = list(tree.iter(tag='item'))  #取得item標籤內容
        message = ''
        for i in range(1,3):
            title = items[i][0].text  #期別
            ptext = items[i][2].text  #中獎號碼
            ptext = ptext.replace('<p>','').replace('</p>','\n')
            message = message + title + '月\n' + ptext + '\n'
        message = message[:-2]
    except:
        print('讀取發票號碼發生錯誤！')

def show3digit(mtext, userid):
    try:
        content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
        tree = ET.fromstring(content.text)
        items = list(tree.iter(tag='item'))  #取得item標籤內容
        ptext = items[0][2].text  #中獎號碼
        ptext = ptext.replace('<p>','').replace('</p>','')
        temlist = ptext.split('：')
        prizelist = []  #特別獎或特獎後三碼
        prizelist.append(temlist[1][5:8])
        prizelist.append(temlist[2][5:8])
        prize6list1 = []  #頭獎後三碼六獎中獎號碼
        for i in range(3):
            prize6list1.append(temlist[3][9*i+5:9*i+8])
        prize6list2 = temlist[4].split('、')  #增開六獎
        sql_cmd = "update users set state='no', digit3='no' where uid='" + userid +"'"
        db.engine.execute(sql_cmd)
        if mtext in prizelist:
            message = '符合特別獎或特獎後三碼，請繼續輸入發票前五碼！'
            sql_cmd = "update users set state='special', digit3='" + mtext + "' where uid='" + userid +"'"
            db.engine.execute(sql_cmd)
        elif mtext in prize6list1:
            message = '恭喜！至少中六獎，請繼續輸入發票前五碼！'
            sql_cmd = "update users set state='head', digit3='" + mtext + "' where uid='" + userid +"'"
            db.engine.execute(sql_cmd)
        elif mtext in prize6list2:
            message = '恭喜！此張發票中了六獎！'
        else:
            message = '很可惜，未中獎。請輸入下一張發票最後三碼。'
    except:
        print('讀取發票號碼發生錯誤！')

def show5digit(mtext, userid, mode, digit3):
    try:
        sql_cmd = "select * from users where uid='" + userid + "'"
        if mode == 'no':
            print('請先輸入發票最後三碼！')
        else:
            try:
                content = requests.get('http://invoice.etax.nat.gov.tw/invoice.xml')
                tree = ET.fromstring(content.text)  #解析DOM
                items = list(tree.iter(tag='item'))  #取得item標籤內容
                ptext = items[0][2].text  #中獎號碼
                ptext = ptext.replace('<p>','').replace('</p>','')
                temlist = ptext.split('：')
                special1 = temlist[1][0:5]  #特別獎前五碼
                special2 = temlist[2][0:5]  #特獎前五碼
                prizehead = []  #頭獎
                for i in range(3):
                    prizehead.append(temlist[3][9*i:9*i+8])
                sflag = False  #記錄是否中特別獎或特獎
                if mode=='special' and mtext==special1:
                    message = '恭喜！此張發票中了特別獎！'
                    sflag = True
                elif mode=='special' and mtext==special2:
                    message = '恭喜！此張發票中了特獎！'
                    sflag = True
                if mode=='special' and sflag==False:
                    message = '很可惜，未中獎。請輸入下一張發票最後三碼。'
                elif mode=='head' and sflag==False:
                    for i in range(3):
                        if digit3 == prizehead[i][5:8]:
                            pnumber = prizehead[i]  #中獎的頭獎號碼
                            break
                    if mtext == pnumber[:5]:
                        message = '恭喜！此張發票中了頭獎！'
                    elif mtext[1:5] == pnumber[1:5]:
                        message = '恭喜！此張發票中了二獎！'
                    elif mtext[2:5] == pnumber[2:5]:
                        message = '恭喜！此張發票中了三獎！'
                    elif mtext[3:5] == pnumber[3:5]:
                        message = '恭喜！此張發票中了四獎！'
                    elif mtext[4] == pnumber[4]:
                        message = '恭喜！此張發票中了五獎！'
                    else:
                        message = '恭喜！此張發票中了六獎！'
                print(message)
            except:
                print('讀取發票號碼發生錯誤！')
    except:
        sql_cmd = "update users set set state='no', digit3='no' where uid='" + userid +"'"
        db.engine.execute(sql_cmd)
        print('模式文字檔讀取錯誤！')


print('\n顯示本期中獎號碼')
showCurrent()

'''
print('\n顯示前期中獎號碼')
showOld()
'''

'''
    elif len(mtext) == 3 and mtext.isdigit():
        show3digit(mtext, userid)

    elif len(mtext) == 5 and mtext.isdigit():
        show5digit(mtext, userid, mode, digit3)
'''



