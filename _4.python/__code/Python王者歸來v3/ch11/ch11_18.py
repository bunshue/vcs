# ch11_18.py
def build_vip(id, name, tel = ''):
    """ 建立VIP資訊 """
    vip_dict = {'VIP_ID':id, 'Name':name}
    if tel:
        vip_dict['Tel'] = tel
    return vip_dict

while True:
    print("建立VIP資訊系統")
    idnum = input("請輸入ID: ")
    name = input("請輸入姓名: ")    
    tel = input("請輸入電話號碼: ")        # 如果直接按Enter可不建立此欄位
    member = build_vip(idnum, name, tel)   # 建立字典
    print(member, '\n')
    repeat = input("是否繼續(y/n)? 輸入非y字元可結束系統: ")
    if repeat != 'y':
        break

print("歡迎下次再使用")

