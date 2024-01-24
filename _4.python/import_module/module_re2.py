import sys

import re

'''
def multiply(m):
    v = int(m.group())
    return str(v * 2)

def getVid(url):
    string strRegex = "(?<=id_)(\\w+)";
    Regex reg = new Regex(strRegex);
    Match match = reg.Match(url);
    return match.ToString();


print("正規表示式的使用")
url = "http://v.youku.com/v_show/id_XNzk2NTI0MzMy.html";
vid = getVid(url);
print("vid : " + vid)


print("取得email帳號")

#取得email帳號

senderEmail = @"david@insighteyes.com";
string[] sendFromUser = senderEmail.Split('@');
int len = sendFromUser.Length;
print("len = " + len.ToString())
int i;
for (i = 0; i < len; i++)
{
print("i = " + i.ToString() + "\t" + sendFromUser[i])
}


print("用Regular Expression拆解e-mail帳號")

List<string> emailList = new List<string>();
email = "xue@163.,xue@163.com12,2707@qq.com,,xue@yahoo.com.cn,xue@163.com,xue@163.com12";
#  Regex reg2 = new Regex(@"^\da-zA-Z_]+@([-\dA-Za-z]+\.)+[a-zA-Z]{2,}$");驗證email的正則表達式  

Regex reg = new Regex(@"(?<email>[\da-zA-Z_]+@([-\dA-Za-z]+\.)+[a-zA-Z]{2,})");
Match m = reg.Match(email);
foreach (Match item in reg.Matches(email))
{
emailList.Add(item.Groups["email"].Value);
}
len = emailList.Count;
print("共取得 : " + len.ToString() + " 個帳號")
for (i = 0; i < len; i++)
{
print("i = " + i.ToString() + "\t" + emailList[i])
}
'''

print("正規表示式的使用")

'''
text = 'tem12po'
pattern = r'[a-z]+'
txt = re.match(pattern, text)
print(txt.group()) # <re.Match object; span=(0, 3), match='tem'>
'''

#正規表示式的使用

#正規表示式

#使用方法
#Regex.Match("String", @"正規表示式").ToString();

text = "USA stands for the United States of America with 50 states and 330 millions people.";

#text = 'tem12po'
#pattern = r'[a-z]+'
#txt = re.match(pattern, text)
#print(txt) # <re.Match object; span=(0, 3), match='tem'>


#只提出字串最前面或最後面的英文
pattern = r"[A-Z]+"
txt = re.match(pattern, text)
print("結果 : ", txt.group())

#只提出字串最前面或最後面的數字
pattern = r"[\d_]+"
txt = re.match(pattern, text)
print("ddd結果 : ", txt)

#其他規則
text = "123ABC456DEF"
pattern = r"[A-Z]+[0-9]+"
txt = re.match(pattern, text)   #Output:"ABC456"
print("ddd結果 : ", txt)

text = "123ABC456DeF"
pattern = r"[0-9A-Z]+"
txt = re.match(pattern, text)   #Output:"123ABC456D"
print("結果 : ", txt.group())

text = "123ABC456DeF"
pattern = r"[0-9A-Za-z]+"
txt = re.match(pattern, text)   #Output:"123ABC456DeF"
print("結果 : ", txt.group())

text = "ABC123D"
pattern = r"[A-Z]+"
txt = re.match(pattern, text)   #Output:"123ABC456DeF"
print("結果 : ", txt.group())

text = "ABC123"
pattern = r"[A-Z]+"
txt = re.match(pattern, text)   #Output:"123ABC456DeF"
print("結果 : ", txt.group())

text = "123ABC456DEF"
pattern = r"[A-Z]+[0-9]+"
txt = re.match(pattern, text)   #Output:"123ABC456DeF"
print("ddd結果 : ", txt)

text = "123ABC"
pattern = r"\d"
txt = re.match(pattern, text)   #Output:"123ABC456DeF"
print("結果 : ", txt.group(), "\t數字")

text = "ABC 123"
pattern = r"[A-Z]+"
txt = re.match(pattern, text)   #Output:"123ABC456DeF"
print("結果 : ", txt.group())

text = "123ABC456-DeF"
pattern = r"[0-9A-Za-z\-]+"
txt = re.match(pattern, text)   #Output:"123ABC456DeF"
print("結果 : ", txt.group())


print("檢查台灣手機號碼")
'''
text = "0922123456";

print("Text = " + text)
bool match;
match = System.Text.RegularExpressions.Regex.IsMatch(text, @"^09[0-9]{8}$");
if (match == true)
{
print("OK")
}
else
{
print("NG")
}


print("檢查中國手機號碼")

text = "13987654321";

print("Text = " + text)

if (!IsHandset(text))
{
print("NG")
}
else
{
print("OK")
}

print("檢查是否為數值")

text = "0x1234";

print("Text = " + text)

if (Regex.IsMatch(text, @"^[\d,\.]+$"))
{
print("是數值")
}
else
{
print("不是數值")
}
'''



import re

msg = 'John and Tom will attend my party tonight. John is my best friend.'
pattern = 'John|Tom'                # 搜尋John和Tom
txt = re.findall(pattern, msg)      # 傳回搜尋結果
print(txt)
pattern = 'Mary|Tom'                # 搜尋Mary和Tom
txt = re.findall(pattern, msg)      # 傳回搜尋結果
print(txt)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_11.py

# ch16_11.py
import re

msg = 'john and TOM will attend my party tonight. JOHN is my best friend.'
pattern = 'John|Tom'                        # 搜尋John和Tom
txt = re.findall(pattern, msg, re.I)        # 傳回搜尋忽略大小寫的結果
print(txt)
pattern = 'Mary|tom'                        # 搜尋Mary和tom
txt = re.findall(pattern, msg, re.I)        # 傳回搜尋忽略大小寫的結果
print(txt)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_12.py

# ch16_12.py
import re

def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:         # 搜尋失敗
        print("搜尋失敗 ",txt)
    else:                   # 搜尋成功
        print("搜尋成功 ",txt.group())

msg1 = 'son'
msg2 = 'sonson'
msg3 = 'sonsonson'
msg4 = 'sonsonsonson'
msg5 = 'sonsonsonsonson'
pattern = '(son){3,5}'
searchStr(pattern,msg1)
searchStr(pattern,msg2)
searchStr(pattern,msg3)
searchStr(pattern,msg4)
searchStr(pattern,msg5)


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_13.py

# ch16_13.py
import re

def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:         # 搜尋失敗
        print("搜尋失敗 ",txt)
    else:                   # 搜尋成功
        print("搜尋成功 ",txt.group())

msg = 'sonsonsonsonson'
pattern = '(son){3,5}'
searchStr(pattern,msg)


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_14.py

# ch16_14.py
import re

def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:         # 搜尋失敗
        print("搜尋失敗 ",txt)
    else:                   # 搜尋成功
        print("搜尋成功 ",txt.group())

msg = 'sonsonsonsonson'
pattern = '(son){3,5}?'     # 非貪婪模式
searchStr(pattern,msg)


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_15.py

# ch16_15.py
import re
# 測試1將字串從句子分離
msg = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = '\w+'                    # 不限長度的單字
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2將John開始的字串分離
msg = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = 'John\w*'                # John開頭的單字
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_16.py

# ch16_16.py
import re

msg = '1 cat, 2 dogs, 3 pigs, 4 swans'
pattern = '\d+\s\w+'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_17.py

# ch16_17.py
import re
# 測試1搜尋[aeiouAEIOU]字元
msg = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = '[aeiouAEIOU]'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2搜尋[2-5.]字元
msg = '1. cat, 2. dogs, 3. pigs, 4. swans'
pattern = '[2-5.]'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_18.py

# ch16_18.py
import re
# 測試1搜尋不在[aeiouAEIOU]的字元
msg = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = '[^aeiouAEIOU]'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2搜尋不在[2-5.]的字元
msg = '1. cat, 2. dogs, 3. pigs, 4. swans'
pattern = '[^2-5.]'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_19.py

# ch16_19.py
import re
# 測試1搜尋John字串在最前面
msg = 'John will attend my party tonight.'
pattern = '^John'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2搜尋John字串不是在最前面
msg = 'My best friend is John'
pattern = '^John'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_2.py

# ch16_2.py
def taiwanPhoneNum(string):
    """檢查是否有含手機聯絡資訊的台灣手機號碼格式"""
    if len(string) != 12:       # 如果長度不是12
        return False            # 傳回非手機號碼格式
    
    for i in range(0, 4):       # 如果前4個字出現非數字字元
        if string[i].isdecimal() == False:
            return False        # 傳回非手機號碼格式
        
    if string[4] != '-':        # 如果不是'-'字元
        return False            # 傳回非手機號碼格式
   
    for i in range(5, 8):       # 如果中間3個字出現非數字字元
        if string[i].isdecimal() == False:
            return False        # 傳回非手機號碼格

    if string[8] != '-':        # 如果不是'-'字元
        return False            # 傳回非手機號碼格式

    for i in range(9, 12):      # 如果最後3個字出現非數字字元
        if string[i].isdecimal() == False:
            return False        # 傳回非手機號碼格
    return True                 # 通過以上測試

def parseString(string):
    """解析字串是否含有電話號碼"""
    notFoundSignal = True       # 註記沒有找到電話號碼為True
    for i in range(len(string)):  # 用迴圈逐步抽取12個字元做測試
        msg = string[i:i+12]
        if taiwanPhoneNum(msg):
            print(f"電話號碼是: {msg}")
            notFoundSignal = False        
    if notFoundSignal:          # 如果沒有找到電話號碼則列印
        print(f"{string} 字串不含電話號碼")

msg1 = 'Please call my secretary using 0930-919-919 or 0952-001-001'
msg2 = '請明天17:30和我一起參加明志科大教師節晚餐'
msg3 = '請明天17:30和我一起參加明志科大教師節晚餐, 可用0933-080-080聯絡我'
parseString(msg1)
parseString(msg2)
parseString(msg3)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_20.py

# ch16_20.py
import re
# 測試1搜尋最後字元是非英文字母數字和底線字元
msg = 'John will attend my party 28 tonight.'
pattern = '\W$'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2搜尋最後字元是非英文字母數字和底線字元
msg = 'I am 28'
pattern = '\W$'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試3搜尋最後字元是數字
msg = 'I am 28'
pattern = '\d$'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試4搜尋最後字元是數字
msg = 'I am 28 year old.'
pattern = '\d$'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_21.py

# ch16_21.py
import re
# 測試1搜尋開始到結尾皆是數字的字串
msg = '09282028222'
pattern = '^\d+$'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2搜尋開始到結尾皆是數字的字串
msg = '0928tuyr990'
pattern = '^\d+$'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_22.py

# ch16_22.py
import re
msg = 'cat hat sat at matter flat'
pattern = '.at'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_23.py

# ch16_23.py
import re

msg = 'Name: Jiin-Kwei Hung Address: 8F, Nan-Jing E. Rd, Taipei'
pattern = 'Name: (.*) Address: (.*)'
txt = re.search(pattern,msg)      # 傳回搜尋結果
Name, Address = txt.groups()
print("Name:    ", Name)
print("Address: ", Address)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_24.py

# ch16_24.py
import re
#測試1搜尋除了換列字元以外字元
msg = 'Name: Jiin-Kwei Hung \nAddress: 8F, Nan-Jing E. Rd, Taipei'
pattern = '.*'
txt = re.search(pattern,msg)           # 傳回搜尋不含換列字元結果
print("測試1輸出: ", txt.group())
#測試2搜尋包括換列字元
msg = 'Name: Jiin-Kwei Hung \nAddress: 8F, Nan-Jing E. Rd, Taipei'
pattern = '.*'
txt = re.search(pattern,msg,re.DOTALL) # 傳回搜尋含換列字元結果
print("測試2輸出: ", txt.group())




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_25.py

# ch16_25.py
import re
#測試1搜尋使用re.match()
msg = 'John will attend my party tonight.'  # John是第一個字串
pattern = 'John'
txt = re.match(pattern,msg)                 # 傳回搜尋結果
if txt != None:
    print("測試1輸出: ", txt.group())
else:
    print("測試1搜尋失敗")
#測試2搜尋使用re.match()
msg = 'My best friend is John.'             # John不是第一個字串
txt = re.match(pattern,msg,re.DOTALL)       # 傳回搜尋結果
if txt != None:
    print("測試2輸出: ", txt.group())
else:
    print("測試2搜尋失敗")







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_26.py

# ch16_26.py
import re
#測試1搜尋使用re.match()
msg = 'John will attend my party tonight.'  
pattern = 'John'
txt = re.match(pattern,msg)                 # re.match()
if txt != None:
    print("使用re.match()輸出MatchObject物件:  ", txt)
else:
    print("測試1搜尋失敗")
#測試1搜尋使用re.search()
txt = re.search(pattern,msg)                # re.search()
if txt != None:
    print("使用re.search()輸出MatchObject物件: ", txt)
else:
    print("測試1搜尋失敗")







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_27.py

# ch16_27.py
import re
#測試1搜尋使用re.match()
msg = 'John will attend my party tonight.'  
pattern = 'John'
txt = re.match(pattern,msg)                 # re.match()
if txt != None:
    print("搜尋成功字串的起始索引位置 :  ", txt.start())
    print("搜尋成功字串的結束索引位置 :  ", txt.end())
    print("搜尋成功字串的結束索引位置 :  ", txt.span())
#測試2搜尋使用re.search()
msg = 'My best friend is John.'  
txt = re.search(pattern,msg)                # re.search()
if txt != None:
    print("搜尋成功字串的起始索引位置 :  ", txt.start())
    print("搜尋成功字串的結束索引位置 :  ", txt.end())
    print("搜尋成功字串的結束索引位置 :  ", txt.span())









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_28.py

# ch16_28.py
import re
#測試1取代使用re.sub()結果成功
msg = 'Eli Nan will attend my party tonight. My best friend is Eli Nan'  
pattern = 'Eli Nan'                 # 欲搜尋字串        
newstr = 'Kevin Thomson'            # 新字串
txt = re.sub(pattern,newstr,msg)    # 如果找到則取代
if txt != msg:                      # 如果txt與msg內容不同表示取代成功
    print("取代成功: ", txt)        # 列出成功取代結果
else:
    print("取代失敗: ", txt)        # 列出失敗取代結果
#測試2取代使用re.sub()結果失敗  
pattern = 'Eli Thomson'             # 欲搜尋字串        
txt = re.sub(pattern,newstr,msg)    # 如果找到則取代           
if txt != msg:                      # 如果txt與msg內容不同表示取代成功
    print("取代成功: ", txt)        # 列出成功取代結果
else:
    print("取代失敗: ", txt)        # 列出失敗取代結果




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_29.py

# ch16_29.py
import re
# 使用隱藏文字執行取代
msg = 'CIA Mark told CIA Linda that secret USB had given to CIA Peter.'
pattern = r'CIA (\w)\w*'            # 欲搜尋CIA + 空一格後的名字        
newstr = r'\1***'                   # 新字串使用隱藏文字
txt = re.sub(pattern,newstr,msg)    # 執行取代
print("取代成功: ", txt)            # 列出取代結果



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_3.py

# ch16_3.py
import re

msg1 = 'Please call my secretary using 0930-919-919 or 0952-001-001'
msg2 = '請明天17:30和我一起參加明志科大教師節晚餐'
msg3 = '請明天17:30和我一起參加明志科大教師節晚餐, 可用0933-080-080聯絡我'

def parseString(string):
    """解析字串是否含有電話號碼"""
    pattern = r'\d\d\d\d-\d\d\d-\d\d\d'
    phoneNum = re.search(pattern, string)
    if phoneNum != None:        # 如果phoneNum不是None表示取得號碼
        print(f"電話號碼是: {phoneNum.group()}")
    else:
        print(f"{string} 字串不含電話號碼")

parseString(msg1)
parseString(msg2)
parseString(msg3)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_30.py

# ch16_30.py
import re

msg = '''02-88223349,
        (02)-26669999,
        02-29998888 ext 123,
        1234567899999,
        02 33887766 ext. 1234,
        02 33887799 ext. 12345,
        12345,
        123'''
pattern = r'''(
    (\d{2}|\(\d{2}\))?              # 區域號碼
    (\s|-)?                         # 區域號碼與電話號碼的分隔符號
    \d{8}                           # 電話號碼
    (\s*(ext|ext.)\s*\d{2,4})?      # 2-4位數的分機號碼
    )'''
phoneNum = re.findall(pattern, msg, re.VERBOSE)     # 傳回搜尋結果
print("以下是符合的電話號碼")
for num in phoneNum:
    print(num[0])





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_31.py

# ch16_31.py
import re

msg = '''02-88223349,
        (02)-26669999,
        02-29998888 ext 123,
        1234567899999,
        02 33887766 ext. 1234,
        02 33887799 ext. 12345,
        12345,
        123'''
pattern = r'''(
    (\d{2}|\(\d{2}\))?              # 區域號碼
    (\s|-)?                         # 區域號碼與電話號碼的分隔符號
    \b\d{8}\b                       # 電話號碼
    (\s*(ext|ext.)\s*\d{2,4}\b)?    # 2-4位數的分機號碼
    )'''
phoneNum = re.findall(pattern, msg, re.VERBOSE)     # 傳回搜尋結果
print("以下是符合的電話號碼")
for num in phoneNum:
    print(num[0])





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_32.py

# ch16_32.py
import re

msg = '''txt@deepwisdom.comyyy.twkkk,
         ser@deepmind.com.tw,
         aaa@gmail.comcomkk,
         kkk@gmail.com,
         abc@aa,
         abcdefg'''
pattern = r'''(
    [a-zA-Z0-9_.]+                  # 使用者帳號
    @                               # @符號
    [a-zA-Z0-9-.]+                  # 主機域名domain
    [\.]                            # .符號
    [a-zA-Z]{2,4}\b                 # 可能是com或edu或其它
    ([\.])?                         # .符號, 也可能無特別是美國
    ([a-zA-Z]{2,4}\b)?              # 國別
    )'''
eMail = re.findall(pattern, msg, re.VERBOSE)     # 傳回搜尋結果
print("以下是符合的電子郵件地址")
for mail in eMail:
    print(mail[0])




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_33.py

# ch16_33.py
import re                   

# 定義一個函數用於重命名檔案串列
def rename_files(files):
    # 定義正則表達式模式匹配檔案名的一部分
    # (\w+)   匹配一個或多個單詞字元(字母、數字或底線)
    # (\d{4}) 匹配四位數字 (代表年份)
    # (\d{2}) 匹配兩位數字 (代表月份)
    pattern = r"(\w+)_(\d{4})_(\d{2})"
    for file in files:                              # 遍歷檔案串列
        # 使用 sub() 函數替換匹配的名稱
        # \1, \2, \3 分別對應第一、第二、第三個捕獲組匹配的內容
        # 這裡將 底線( _ ) 替換為 ( - )
        new_name = re.sub(pattern, r"\1-\2-\3", file)
        print(f"Old : {file},   New: {new_name}")   # 輸出舊和新檔名

# 檔案名稱串列
files = [
    "report_2023_04.pdf",
    "report_2023_05.pdf",
    "summary_2023_04.docx"
]

rename_files(files)  # 呼叫函數, 傳入檔案名稱串列

# 輸出
# Old: report_2023_04.pdf,  New: report-2023-04.pdf
# Old: report_2023_05.pdf,  New: report-2023-05.pdf
# Old: summary_2023_04.docx,  New: summary-2023-04.docx






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_34.py

# ch16_34.py
import re

def validate_and_format_credit_card(number):
    # 定義Visa信用卡號碼的正則表達式, Visa卡號以4開頭, 並有16位數字
    pattern = r"^(?:4[0-9]{12}(?:[0-9]{3})?)$"  

    # 使用match方法檢查提供的卡號是否符合正則表達式模式。
    match = re.match(pattern, number)
    if match:
        # 如果匹配成功，使用findall方法分組每四位數字
        # 然後用join方法將這些組用 "-" 連接成一個格式化的字串
        formatted = "-".join(re.findall(r"....", number))
        return True, formatted  # 返回一個元組和驗證成功格式化的卡號
    return False, None          # 如果匹配不成功, 返回False和None

# 測試卡號
card_number = "4111111111111111"
is_valid, formatted = validate_and_format_credit_card(card_number)
print(is_valid, formatted)      # 輸出結果應該為True和格式化後的卡號







print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_35.py

# ch16_35.py
import re

def clean_text(text):
    # 刪除不可列印字元和特殊符號, 只保留字母、數字和空格
    pattern = r"[^\w\s]"
    cleaned_text = re.sub(pattern, "", text)
    return cleaned_text

dirty_data = "Name: John Doe; Age: 30; %Salary: $5000"
print(clean_text(dirty_data))
# 輸出: Name John Doe Age 30 Salary 5000



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_4.py

# ch16_4.py
import re

msg1 = 'Please call my secretary using 0930-919-919 or 0952-001-001'
msg2 = '請明天17:30和我一起參加明志科大教師節晚餐'
msg3 = '請明天17:30和我一起參加明志科大教師節晚餐, 可用0933-080-080聯絡我'

def parseString(string):
    """解析字串是否含有電話號碼"""
    pattern = r'\d\d\d\d-\d\d\d-\d\d\d'
    phoneNum = re.findall(pattern, string)
    if phoneNum != None:        # 如果phoneNum不是None表示取得號碼
        print(f"電話號碼是: {phoneNum}")
    else:
        print(f"{string} 字串不含電話號碼")

parseString(msg1)
parseString(msg2)
parseString(msg3)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_5.py

# ch16_5.py
import re

msg1 = 'Please call my secretary using 0930-919-919 or 0952-001-001'
msg2 = '請明天17:30和我一起參加明志科大教師節晚餐'
msg3 = '請明天17:30和我一起參加明志科大教師節晚餐, 可用0933-080-080聯絡我'

def parseString(string):
    """解析字串是否含有電話號碼"""
    pattern = r'\d{4}-\d{3}-\d{3}'
    phoneNum = re.findall(pattern, string)   # 用串列傳回搜尋結果
    print(f"電話號碼是: {phoneNum}")         # 串列方式顯示電話號碼

parseString(msg1)
parseString(msg2)
parseString(msg3)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_6.py

# ch16_6.py
import re

msg = 'Please call my secretary using 02-26669999'
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.search(pattern, msg)           # 傳回搜尋結果

print(f"完整號碼是: {phoneNum.group()}")     # 顯示完整號碼
print(f"完整號碼是: {phoneNum.group(0)}")    # 顯示完整號碼
print(f"區域號碼是: {phoneNum.group(1)}")    # 顯示區域號碼
print(f"電話號碼是: {phoneNum.group(2)}")    # 顯示電話號碼




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_7.py

# ch16_7.py
import re

msg = 'Please call my secretary using 02-26669999 or 02-11112222'
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.findall(pattern, msg)           # 傳回搜尋結果
print(phoneNum)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_8.py

# ch16_8.py
import re

msg = 'Please call my secretary using 02-26669999'
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.search(pattern, msg)      # 傳回搜尋結果
areaNum, localNum = phoneNum.groups()   # 留意是groups()
print(f"區域號碼是: {areaNum}")         # 顯示區域號碼
print(f"電話號碼是: {localNum}")        # 顯示電話號碼




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch16\ch16_9.py

# ch16_9.py
import re

msg = 'Please call my secretary using (02)-26669999'
pattern = r'(\(\d{2}\))-(\d{8})'
phoneNum = re.search(pattern, msg)       # 傳回搜尋結果
areaNum, localNum = phoneNum.groups()    # 留意是groups()
print(f"區域號碼是: {areaNum}")          # 顯示區域號碼
print(f"電話號碼是: {localNum}")         # 顯示電話號碼




print("------------------------------------------------------------")  # 60個

